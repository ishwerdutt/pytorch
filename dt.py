# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:53:48 2024

@author: irish
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz


iris = load_iris()

X = iris.data[:, :]
y = iris.target


clf.fit(X, y)


export_graphviz(
    clf,
    feature_names=iris.feature_names,
    class_names = iris.target_names,
    rounded = True,
    filled = True
    )

