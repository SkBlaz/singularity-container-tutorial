# Running existing images

Assuming Bob has the file named _tree.py_. Assuming this piece of code accepts command line parameters specifying data and target space, performs three fold cross validation and returns the result, so something like:

```bash
python tree.py --super_big_data somedata.dat --super_multitarget_space targets.dat
```

and returns something in the lines of:

```
RESULT10fCV 1 0.89
RESULT10fCV 2 0.85
RESULT10fCV 3 0.81
```

Of course, Bob is interested in obtaining the above results of cross validation for _some new data_. Assuming that bob is not able to exactly replicate the environment on his own for one of the following reasons:

1. Some driver conflict prohibits installation of one of the libraries
2. He's unable to install all requirements.txt directly for whatever reason
3. He's lazy

We are able to present a simple solution - the *Singularity* container. The idea is the following:
1. Precompile a Python environment with minimal spatial overhead and all required libraries
2. Share the environment as a *single file*

## What are singularity files?
Singularity files are *images*, just like e.g., your favourite Star Wars movie DVD.
Given an example Singularity image, e.g., *OurSingularityImage.sif*, the above piece of code can be run as:

```
singularity exec OurSingularityImage.sif python tree.py --super_big_data Bob_somedata.dat --super_multitarget_space Bob_targets.dat
```

+ `singularity` = call of the tool
+ `exec` = flag to execute a given command (there is also `run`)
+ `OurSingularityImage.sif` = our environment image.

and the output should be, of course, different. E.g.,

```
RESULT10fCV 1 0.31
RESULT10fCV 2 0.32
RESULT10fCV 3 0.33
```

That's it. Bob was able to **replicate** our environment and run the codebase.