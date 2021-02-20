# Hyperparameter optimization
In machine learning and many other fields, methods often come with a predefined collection of tunable hyperparameters.
Either the user can fine-tune these by hand, however, this is somewhat counterproductive. What if we could, at least to some extent,
automate this process?

## Problem setting
In the folder `optimization` you can find the files we'll need for this tutorial. The files are:
1. environment.dsc - the Singularity description file
2. build_image.sh - the file for building an image from the .dsc file
3. genes.tsv - a .tsv file containing the input data
4. learners.py - a file for evaluation of learning algorithms
5. clusterjob.xrsl - the .xrsl job description file

And that's it! Our plan is to:

1. Build the image and test the learning locally
2. Upload the data and the image to the dCache server
3. Send a few jobs and retrieve the results
4. Analyse the obtained results

Let's begin!


### Building and testing the image
As you know by now, we can build the image from the environment.dsc file as follows.


```
singularity build MLImage.sif environment.dsc
```

This should finish without errors, yielding a fresh new .sif file.

### Local testing

The provided `learners.py` works for example as follows:

```
python learners.py --dataset genes.tsv --num_trees 100
```

Here, we are using the provided `genes.tsv` data set and are setting the number of trees (hyperparameter) to `100`.
If you run this via the compiled image:

```
singularity exec learners.py --dataset genes.tsv --num_trees 100
```
The output should be in the following form:

```
RESULT_LINE genes 100 0.79
```
Where the first entry (`RESULT_LINE`) is the flag of the result line, `genes` the name of the data set, `100` the hyperparameter value and `0.79` a performance metric (e.g., accuracy). Our goal is to produce multiple such jobs, send them to the grid, fetch the results and identify which hyperparameter yields the best accuracy. At this point, let's assume the learners.py offers an unbiased estimate of the accuracy as this is not the key focus of this tutorial.

## Preparing jobs
We will be using the `arc` client via .xrsl job descriptions, which for example look like:

```
&
(executable = "runfile.sh")
(inputFiles =
  ("learners.py" "learners.py")
  ("runfile.sh" "runfile.sh")
  ("minimalML.sif" "gsiftp://dcache.arnes.si/data/arnes.si/gen.vo.sling.si/skrlj_virtual_envs/minimalML.sif")
)
(walltime = "5 hours")
(memory=1000)
(join="yes")
(stdout="job.log")
(count=8)
(countpernode=8)
(cache=no)
(jobname="Singularity tutorial - learning")
```

Here, we can see that in the first part, a runfile script needs to be provided. In our case, `run.sh` can be as simple as:
```
singularity exec minimalML.sif python3 learners.py --dataset genes.tsv --num_trees 100
```
Looks familiar? It should! This script simply executes a single command in our case. As we are performing a benchmark of sorts, let's explore more hyperparameter values automatically (within a single job!):

```
for j in `seq 10 100`; do singularity exec minimalML.sif python3 learners.py --dataset genes.tsv --num_trees $j;done
```

This generates multiple jobs, which will all be executed within the same `xrsl` job.
Let's remind ourselves of the basic commands for operating with the `arc` client.

```
arccp somefile dcacheLocation (copy e.g., image to the cluster)
```

```
arcsub -c clusterName -j job.xrsl (submit the job to a specific cluster)
```

```
arcget -a (get all jobs back)
```

```
arcproxy -S proxyID (establish proxy for arc to communicate with the grid)
```

## Running the jobs
Let's first sync our image to the cluster:

```
arccp minimalML.sif gsiftp://dcache.arnes.si/data/arnes.si/gen.vo.sling.si/skrlj_virtual_envs/
```

Next, let's send the job to the cluster called `trebuchet`,
```
arcsub -c trebuchet.ijs.si clusterjob.xrsl -o jobID.txt
```

The `benchmarkJob.txt` is the name of the job storage file. We can monitor wheter it runs OK via:
```
arcstat -i jobID.txt
```

Once it finishes, let's go into `cluster_results` folder and run:

```
arcget -i jobID.txt
```

## To find the best performing configuration, we can for example do the following:
```
cat job.log | grep 'RESULT_LINE' | sort -k5 -n | tail
```
resulting in:

```
RESULT_LINE	genes	RF	70	0.9649122807017545
RESULT_LINE	genes	RF	75	0.9649122807017545
RESULT_LINE	genes	RF	90	0.9649122807017545
RESULT_LINE	genes	RF	92	0.9649122807017545
RESULT_LINE	genes	RF	98	0.9649122807017545
RESULT_LINE	genes	RF	32	0.9666666666666666
RESULT_LINE	genes	RF	77	0.9666666666666666
RESULT_LINE	genes	RF	83	0.9666666666666666
RESULT_LINE	genes	RF	36	0.9666666666666668
RESULT_LINE	genes	RF	52	0.9666666666666668
```