# Scaling to GPUs

There are two additional steps to ensure Singularity is able to exploits the power of GPUs. First, the environment must support the cuda drivers. By far, the simplest way is to just change the origin image. For example, by adapting [the compilation](compilation.md) example,


```
BootStrap: docker
From: nvcr.io/nvidia/cuda:11.1.1-devel-ubuntu20.04 # note this

%environment
export LC_ALL=C # Specification of environment variables

%post
# Some generic Ubuntu libraries
apt-get update
apt-get install -y libhdf5-dev graphviz locales python3-dev python3-pip curl
apt-get clean

# Python requirements
pip3 torch torchvision

```
Assuming the compiled image is named *coolCudaImage.sif*.
See all [cuda images](https://ngc.nvidia.com/catalog/containers?orderBy=modifiedDESC&pageNumber=0&query=&quickFilter=containers&filters=) if needed.

When running the containers, **be careful** to include the "-nv" tag.

```
singularity exec --nv coolCudaImage.sif treeGPU.py --super_big_data Bob_somedata.dat --super_multitarget_space Bob_targets.dat
```

And that's it.