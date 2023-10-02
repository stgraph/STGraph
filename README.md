<div align="center">
  <p align="center">
    ⚠️ <b>DISCLAIMER</b> ⚠️
  <p>
    <p><em>This is an anonymized fork of the original repository for purposes of submission to double blind conferences.</em></p>
</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/stgraph/STGraph/assets/146707796/af1646ea-0b9e-442b-9685-aa5a3141a6ab">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/stgraph/STGraph/assets/146707796/287b7f5a-8b4d-4603-b5ae-78c8f5b65f6c">
  <img alt="STGraph Banner" src="https://github.com/stgraph/STGraph/assets/146707796/4fbf5dd5-265f-4931-89a9-f7b515097989">
</picture>


<div align="center">
  <p align="center">
    <a href=""><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/stgraph/STGraph/blob/main/INSTALLATION.md">Installation guide</a>
    ·
    <a href="https://github.com/stgraph/STGraph/issues">Report Bug</a>
    ·
    <a href="https://github.com/stgraph/STGraph/pulls">Pull Requests</a>
  </p>
</div>


# 🌟 STGraph

STGraph is a framework designed for deep-learning practitioners to write and train Graph Neural Networks (GNNs) and Temporal Graph Neural Networks (TGNNs). It is built on top of _Seastar_ and utilizes the vertex-centric approach to produce highly efficient fused GPU kernels for forward and backward passes. It achieves better usability, faster computation time and consumes less memory than state-of-the-art graph deep-learning systems like DGL, PyG and PyG-T.

## Why STGraph

The primary goal of _Seastar_ is more natural GNN programming so that the users learning curve is flattened. Our key observation lies in recognizing that the equation governing a GCN layer, as shown above, takes the form of vertex-centric computation and can be implemented succinctly with only one line of code. Moreover, we can see a clear correspondence between the GNN formulas and the vertex-centric implementations. The benefit is two-fold: users can effortlessly implement GNN models, while simultaneously understanding these models by inspecting their direct implementations.

The _Seastar_ system outperforms state-of-the-art GNN frameworks but lacks support for TGNNs. STGraph bridges that gap and enables users to to develop TGNN models through a vertex-centric approach. STGraph has shown to be significantly faster and more memory efficient that state-of-the-art frameworks like PyG-T for training TGNN models.

## Getting Started

Install, build and train your first TGNN model using STGraph by following the [installation guide](https://github.com/stgraph/STGraph/blob/main/INSTALLATION.md).

## Attributions

| Author(s)                                                                                                                                                                         | Title                                                                                                    | Link(s)                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `Wu, Yidi and Ma, Kaihao and Cai, Zhenkun and Jin, Tatiana and Li, Boyang and Zheng, Chenguang and Cheng, James and Yu, Fan`                                                      | `Seastar: vertex-centric programming for graph neural networks, 2021`                                    | [paper](https://doi.org/10.1145/3447786.3456247), [code](https://zenodo.org/record/4988602)                                      |
| `Wheatman, Brian and Xu, Helen`                                                                                                                                                   | `Packed Compressed Sparse Row: A Dynamic Graph Representation, 2018`                                     | [paper](https://ieeexplore.ieee.org/abstract/document/8547566), [code](https://github.com/wheatman/Packed-Compressed-Sparse-Row) |
| `Sha, Mo and Li, Yuchen and He, Bingsheng and Tan, Kian-Lee`                                                                                                                      | `Accelerating Dynamic Graph Analytics on GPUs, 2017`                                                     | [paper](http://www.vldb.org/pvldb/vol11/p107-sha.pdf), [code](https://github.com/desert0616/gpma_demo)                           |
| `Benedek Rozemberczki, Paul Scherer, Yixuan He, George Panagopoulos, Alexander Riedel, Maria Astefanoaei, Oliver Kiss, Ferenc Beres, Guzmán López, Nicolas Collignon, Rik Sarkar` | `PyTorch Geometric Temporal: Spatiotemporal Signal Processing with Neural Machine Learning Models, 2021` | [paper](https://arxiv.org/pdf/2104.07788.pdf), [code](https://github.com/benedekrozemberczki/pytorch_geometric_temporal)         |
