from sklearn.linear_model import PassiveAggressiveClassifier
clf = PassiveAggressiveClassifier(1.0, True, 5, True, 0, loss='hinge', n_jobs=1, class_weight=None)