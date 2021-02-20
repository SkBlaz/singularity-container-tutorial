## a simple learning evaluation 10f for RF

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score
import numpy as np

def get_score(X, Y):
    """
    A super generic evaluation based on 10 stratified folds with the same seed!
    """

    performance_storage = []
    sss = StratifiedShuffleSplit(n_splits=10, test_size=0.1, random_state=65498)
    print(f"Estimating for {args.num_trees} trees.")
    for train_index, test_index in sss.split(X, Y):
        X_train = X[train_index]
        X_test = X[test_index]
        Y_train = Y[train_index]
        Y_test = Y[test_index]
        clf = RandomForestClassifier(n_estimators = args.num_trees)
        predictions = clf.fit(X_train, Y_train).predict(X_test)
        acc = accuracy_score(predictions, Y_test)
        performance_storage.append(acc)
    return np.mean(performance_storage)        

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_trees",default=100, type = int)
    args = parser.parse_args()
    dataset = load_breast_cancer()
    X = dataset.data
    Y = dataset.target
    score = get_score(X,Y)
    print("\t".join(["RESULT_LINE","genes","RF",str(args.num_trees),str(score)]))
