# Installation Guide

This comprehensive guide will walk you through the installation process for STGraph, along with its essential prerequisites, enabling you to train TGNN models on your local machine. Let's get started.

## STGraph Installation

To download STGraph on your local machine, execute the following command:

```
git clone https://github.com/stgraph/STGraph.git
cd STGraph
```

### STGraph Virtual Environment

It is highly recommended to create a dedicated Python virtual environment for running and developing with STGraph. To create a virtual environment named `stgraph`, you can use either conda or venv.

Using conda:

```
conda create --name stgraph python=3.10
conda activate stgraph
```

### Installing Python Packages

To install the necessary Python packages for STGraph, run the following command. Ensure that you have activated the `stgraph` virtual environment before installing these packages.

```
pip install -r requirements.txt
```

You may encounter some errors or warnings, which you can ignore for now. 

**Installing PyTorch and PyG-T**

It is recommeneded to install PyTorch and PyTorch Geometric Temporal separately. Execute the following commands

```
pip install torch torchvision torchaudio
pip install torch-scatter torch-sparse -f https://data.pyg.org/whl/torch-2.0.0+cu117.html
pip install torch-geometric-temporal
```

### STGraph Graph Packages Installation

Before proceeding with the remaining installation steps, it is crucial to build the shared object (.so) file for the CUDA/C++ extension that implements certain dynamic and static graph representations in STGraph. 

```
cd stgraph/graph/
./build_static.sh
./build_dynamic.sh gpma pcsr
```
Once the build process completes successfully, you can proceed with the remaining installation steps.

### STGraph Package Installation

To complete the installation of the STGraph package, execute the following commands:

```
cd ../..
python3 -m build && pip uninstall stgraph -y && pip install dist/stgraph-1.0.0-py3-none-any.whl
```

After running the above commands, you can verify whether STGraph is installed correctly by executing `pip show stgraph`.

By executing the above instructions, you will have successfully installed STGraph along with all the required packages.

## CUDA Python

STGraph leverages CUDA Python, which encompasses a standardized collection of low-level interfaces, granting complete coverage of and access to the CUDA host APIs within Python. Prior to installing CUDA Python, ensure that your system meets the following requirements:

**Note:**
> STGraph has undergone testing with Python CUDA version 11.7 and above. This installation guide is based on the latest release of Python CUDA, namely version 12.1.0. You can also install Python CUDA for versions 11.7 and above.

### System Requirements

1. **Driver**: Linux (450.80.02 or later) / Windows (456.38 or later)
2. **CUDA Toolkit**: Versions 12.0 to 12.1
3. **Python**: Versions 3.8 to 3.11

### Installation from PyPI

Execute the following command to install CUDA Python via PyPI:

```
pip install cuda-python
```

### Verifying the Installation

To validate the successful installation of Python CUDA, run the provided Python script located within the STGraph directory:

```
cd stgraph/compiler/code_gen/
python3 cuda_check.py
```

If the installation was successful, you should observe the following output. However, please note that the specific output may differ depending on the GPU present in your machine:

```

       Device Property   Value
───────────────────────────────────────────────────
     Number of Devices   1
                  Name   NVIDIA GeForce MX350
    Compute Capability   6.1
  Multiprocessor Count   5
    Concurrent Threads   10240
             GPU Clock   1468.0 MHz
          Memory Clock   3504.0 MHz
          Total Memory   2047.875 MiB
           Free Memory   1641.7216796875 MiB

Note: If either the Total Memory or Free Memory shows 0,
      it indicates that no context has been loaded into the device.
```

With this, you have now completed the installation of STGraph and verified the presence of CUDA Python on your system.

## Running STGraph

To verify the successful installation, let's proceed with running STGraph by training a T-GCN model on the WikiMaths dataset.

```
cd ../../..
cd benchmarking/
chmod u+x verify.sh
./verify.sh
```

Upon executing the above command, it will download the dataset and start training the model. You'll get a table displaying the time taken, MSE and memory consumed for each epoch. Congratulations, STGraph is running properly. 

You might either find that the results shows up as OOM (out of memory). This may happen due to the fact that the GPU does not have enough memory to work with this dataset. You can still confirm whether STGraph works properly by inspecting the CUDA code generated for this T-GCN model. You can view it in the following directory

```
cd static-temporal-tgcn/stgraph/
```

You should find the CUDA code in `egl_kernel.cu` and the PTX file in `egl_kernel.ptx`.

If you encounter any errors while attempting to train the T-GCN model, kindly raise an issue, and our team will promptly assist you.
