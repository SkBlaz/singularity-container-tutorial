# Manipulation of Singularity images
Once Bob understood that Singularity containers can be built, the next natural question that arises is **how can they be manipulated**.

The following collection of examples highlights the key functionality:

## Building Singularity containers on host system
As the user does not necessarily have all the privileges, the question whether a container can still be built arises; the following tag addresses this issue:
```bash
singularity build --fakeroot
```

## Binding directories
What if Bob wishes to present a directory to the singularity environment directly?

```bash

singularity -B /somefolder
```
The `-B` tag offers this functionality.

## What about environment variables?
What if the initially set variables (`%environment`) are not sufficient?

```bash
singularity exec --env
```
More tips and tricks regarding the ENV variables are nicely summarised [here](https://sylabs.io/guides/3.7/user-guide/environment_and_metadata.html).

## Inspecting the definition files
Forgot what the image is exactly?

```bash
singularity inspect -d singularitySimage.sif
```

## What about MPI-related parallelization?
If you are using the same machine for all processes, MPI works fine within the container. For multi-machine parallelism, however, each MPI rank must be a separate container:

```bash
mpirun singularity exec image.sif massivelyParallelTree.py
```

## What about editing an existing image?
What if Bob forgot to install a particular library, and would like to make just this one little fix? Consider the following image:

```bash
sudo singularity build --sandbox minitest docker://ubuntu

```
Note the `--sandbox` option? This enables *editability*. Once having such image,
open the shell with:

```bash
singularity shell --writable minitest
```
and perform any operations needed. The ENV variables are accessible in:

```bash
#!/bin/sh
#custom env code
```
