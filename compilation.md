# Compiling own images

Assuming Bob became a real fan once we've shown him the **container.sif exec** magic.
A new project arrives, where Bob realizes he needs an environment that is different, whilst considering multiple machines. To help him, we suggest the following:

1. Install Singularity across all machines he plans to use ([installation](installation.md))
2. Compile a **new** Singularity container with the newest coolest libraries
3. Proceed as in step [about running the containers](running.md)

## Compiling Singularity images
The key ingredient of each image (similarly to Docker files) are the description files (ending in .dsc). Let's consult the following example:

```
BootStrap: docker
From: ubuntu # We are building an ubuntu-based image

%environment
export LC_ALL=C # Specification of environment variables

%post
# Some generic Ubuntu libraries
apt-get update
apt-get install -y libhdf5-dev graphviz locales python3-dev python3-pip curl
apt-get clean

# Python requirements
pip3 install deap==1.3.0
pip3 install pandas==0.25.0
pip3 install nltk==3.4.4
pip3 install scipy==1.4.0
pip3 install networkx==2.3
pip3 install matplotlib==3.1.0
pip3 install seaborn ## bad practice! Use versions.
pip3 install tqdm==4.40.2
pip3 install numpy
pip3 install gensim
pip3 install umap-learn
pip3 install editdistance
pip3 install nose==1.3.7
pip3 install update-checker>=0.16
pip3 install stopit>=1.1.1
pip3 install joblib>=0.13.2
pip3 install tpot

```

Other container sources:
+ URI beginning with library:// to build from the Container Library
+ URI beginning with docker:// to build from Docker Hub
+ URI beginning with shub:// to build from Singularity Hub

[Other BootStrap modules](https://singularity.lbl.gov/archive/docs/v2-2/bootstrap-image):
+ arch
+ docker
+ debootstrap
+ yum


The description file (assuming it is stored as environment.dsc) is essentially a *recipe* for specifying how the environment should look like. We first install some Unix libraries (apt-get part), followed by python library installation (pip3). Once specified, there is only one line to rule them all:

```
singularity build coolNewImage.sif environment.dsc
```

+ `singularity` = call of the tool
+ `build` = flag to generate an image
+ `coolNewImage.sif` = name of the cool new image
+ `environment.dsc` = environment specification

And that's it. Should all work well, Bob now has **coolNewImage.sif**, a brand new image with which he can perform experiments on all other machines where the singularity was **previously installed**.