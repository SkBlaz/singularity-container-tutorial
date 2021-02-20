for j in `seq 10 100`; do singularity exec minimalML.sif python3 learners.py --num_trees $j;done
