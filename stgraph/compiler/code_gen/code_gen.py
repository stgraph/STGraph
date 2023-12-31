from ..utils import is_const_scalar, ParallelMode
from collections import namedtuple
from .compiler import compile_cuda
from jinja2 import Environment, PackageLoader

EdgeInfo = namedtuple('EdgeInfo', ['load', 'compute', 'inner_write'])
NodeInfo = namedtuple('NodeInfo', ['load', 'compute', 'inner_write'])
ArgInfo = namedtuple('ArgInfo', ['name', 'type', 'is_ptr'])
AggInfo = namedtuple('AggInfo', ['init', 'compute', 'inner_write', 'outter_write'])

const_id = 0
def gen_arg_info(arg):
    if is_const_scalar(arg):
        global const_id
        arg_info = ArgInfo(name='c'+str(const_id), type=str(type(arg)), is_ptr=False)
        const_id += 1
    else:
        arg_info = ArgInfo(name=arg.id, type=str(arg.dtype_str), is_ptr=True)
    return arg_info

def gen_agg_info(stmt, ctx):
    m = stmt.gen_code(ctx)
    if not m:
        raise NotImplementedError('Cannot generate code for', stmt)
    return AggInfo(**m)

def gen_edge_info(stmt, ctx):
    m = stmt.gen_code(ctx)
    if not m:
        raise NotImplementedError('Cannot generate code for', stmt)
    return EdgeInfo(**m)

def gen_node_info(stmt, ctx):
    m = stmt.gen_code(ctx)
    if not m:
        raise NotImplementedError('Cannot generate code for', stmt)
    return NodeInfo(**m)

def gen_code(exe_units, index_type, graph_type):
    '''Generating cuda code by instantiate code template'''
    if not isinstance(exe_units, list):
        exe_units = [exe_units]
    configs = []
    for unit in exe_units:
        if not unit.compiled:
            continue
        arginfos = []
        nodeinfos = []
        agginfos = []
        edgeinfos = []
        for var in unit.kernel_args():
            arginfos.append(gen_arg_info(var))
        ctx = unit.create_context(index_type)
        after_agg = False
        for stmt in unit.program:
            ctx.set_stmt_ctx(stmt)
            if stmt.is_agg():
                agginfos.append(gen_agg_info(stmt, ctx))
                after_agg = True
            elif stmt.is_edgewise():
                edgeinfos.append(gen_edge_info(stmt, ctx))
            elif stmt.is_nodewise():
                if after_agg:
                    nodeinfos.append(gen_node_info(stmt, ctx))
                else:
                    edgeinfos.append(gen_edge_info(stmt, ctx))

        dst_parallel = True if unit.parallel_mode() == ParallelMode.DstParallel else False
        configs.append({
            'kernel_name': unit.kernel_name,
            'index_type' : index_type,
            'args': arginfos,
            'edges': edgeinfos,
            'aggs': agginfos,
            'nodes': nodeinfos,
            'row_offset': 'dst_id' if dst_parallel else 'src_id',
            'init_outter_offset': ctx.param_offset_init + (ctx.dst_var_offset_init if dst_parallel else ctx.src_var_offset_init),
            'col_index': 'src_id' if dst_parallel else 'dst_id',
            'init_inner_offset': (ctx.src_var_offset_init if dst_parallel else ctx.dst_var_offset_init) + ctx.edge_var_offset_init,
            'template_name': ctx.template_name,
            'graph_type': graph_type
        })
    return gen_cuda(configs)

def render_template(config, template_name):
    env = Environment(
    loader=PackageLoader("stgraph.compiler.code_gen"),
    )
    tpl = env.get_template("fa/{}.jinja".format(template_name))
    return tpl.render(**config)

def gen_cuda(configs):
    h = ''
    for config in configs:
        if config['template_name'] == 'fa':
            if config['graph_type'] == 'csr':
                rendered_tpl = render_template(config, "tpl_fa_csr")
            elif config['graph_type'] == 'csr_unsorted':
                rendered_tpl = render_template(config, "tpl_fa_csr_unsorted")
            elif config['graph_type'] == 'pcsr': 
                rendered_tpl = render_template(config, "tpl_fa_pcsr")
            elif config['graph_type'] == 'pcsr_unsorted': 
                rendered_tpl = render_template(config, "tpl_fa_pcsr_unsorted")
            elif config['graph_type'] == 'gpma':   
                rendered_tpl = render_template(config, "tpl_fa_gpma")
            elif config['graph_type'] == 'gpma_unsorted':   
                rendered_tpl = render_template(config, "tpl_fa_gpma_unsorted")
            else:
                raise NotImplementedError('{} Template for {} is not supported'.format(config['template_name'],config['graph_type']))
        elif config['template_name'] == 'v2':
            raise NotImplementedError('{} Template for {} is not supported'.format(config['template_name'],config['graph_type']))
        else:
            raise NotImplementedError('{} Template not supported'.format(config['template_name']))
        h += rendered_tpl
    
    return compile_cuda(h)
