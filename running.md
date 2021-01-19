# Running existing images

Assuming Bob has the file named _tree.py_. Assuming this piece of code accepts command line parameters specifying data and target space, performs three fold cross validation and returns the result, so something like:

```bash
python tree.py --super_big_data somedata.dat --super_multitarget_space targets.dat
```

and returns something in the lines of:

```
RESULT_10fCV 1 0.89
RESULT_10fCV 2 0.85
RESULT_10fCV 3 0.81
```

Of course, Bob is interested in obtaining the above results of cross validation for _some new data_.