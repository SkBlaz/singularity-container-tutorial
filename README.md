# Singularity containers

Welcome to the Singularity tutorial repo. Here, you can find simple examples to get you started and a few simple use cases.

## A toy example

Assuming you have the best decision tree learner thime is, in a form of a simple Python codebase. Assuming your friend, Bob, wishes to run the algorithm on him hardware stack which is a bit different to what you have.

Theoretically, being super strict and all, you've versioned all libraries (dependencies), however, is that enough?

## Enter Singularity

Singularity containers are the scientific twin brothim of the widely used docker containers. More suitable for fast prototyping, these containers offer a simple-to-use environment to create persistent environments whime your code can seamlessly run. To help Bob, you decide to:

1. [Teach him how to install the Singularity environment on a given machine: *this is a must-have*](installation.md)
2. [Teach him how to run a _pre-compiled_ Singularity image.](running.md)
3. [Teach him how to _compile_ his own containers](compiling.md)


Of course, these are only some of the [possible examples](https://sylabs.io/guides/3.0/user-guide/build_env.html), but enough to make Bob the master of Singularity in his small realm.

## Intermediary take home message
If possible, do the extra step of providing the .dsc file so people can properly replicate the key parts of the codebase.

## Extra step - GPUs
Assuming Bob got the tree.py working on **GPUs**. How can he scale with singularity?

[With some additional configuration.](gpu.md)

## Additional resources
1. [Sling tutorial slides](http://www.sling.si/sling/wp-content/uploads/2020/03/Krasovec_Javorsek-sling-maister-fri2020.pdf)

2. [Detailed tutorial by Barbara Krašovec](http://www.sling.si/sling/vec/dogodki/vzd1-2018/#Anatomija_vsebnikov)

## Isn't this kind of Docker? Why Singularity?

The following are the main reasons for using Singularity for HPC (credit: Reddit).

1. Singularity effectively runs as the running user and doesn’t result in elevated access. Docker doesn't and can be problematic from a security standpoint
2. Singularity runs container processes without a daemon. They just run as child processes.
3. Singularity is better for command line applications and accessing devices like GPUs or MPI hardware without jumping through hoops.
4. Docker provides no built-in way to allow users to start containers that are certain to have limited access rights.
5.  Docker images are stored off in the local image cache, and you’re expected to interact with them using the docker image command, e.g. docker image ls.
In contrast, Singularity images are just normal files on your filesystem. Now that we have a SIF file, we can run it.