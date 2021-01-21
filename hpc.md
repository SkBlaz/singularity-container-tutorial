# What about HPC execution?
Assuming Nordugrid cluster architecture, the common way to run code with Singularity is:

## Finding the GPU-capable RTE

```
arcinfo -l cluster_name
```

## Define the GPU-capable container
See [Definition of GPU-based containers](gpu.md)


## Define an xrsl file

```bash

&
  (executable = runfile.sh)
  (jobname = "GPUtest")

  (inputFiles = 
   ("ubuntu_latest.sif" "gsiftp://dcache.arnes.si:2811/data/arnes.si/gen.vo.sling.si/yourname/ubuntu_latest.sif")
   ("bestGPUcodeEver.py" "")
  )
  (stdout=test.log)
  (join=yes)
  (gridtime=100)
  (gmlog=log)
  (cache=no)
  (memory=300)

```

## Running Singularity
Note that for running singularity, you need the following flag (this could be `runfile.sh`):
```bash
singularity exec --nv ubuntu_latest bestGPUcodeEver.py
```

## What in the name is dcache?
Please, see the [Detailed tutorial by Barbara Krašovec](http://www.sling.si/sling/vec/dogodki/vzd1-2018/#Anatomija_vsebnikov)

TLDR: `dcache` offers elegant storage of the images somewhere other clusters can see them. Assuming ARC client, copy the image via:

```bash
arccp gpuImage.sif place_on_the_cluster
```



