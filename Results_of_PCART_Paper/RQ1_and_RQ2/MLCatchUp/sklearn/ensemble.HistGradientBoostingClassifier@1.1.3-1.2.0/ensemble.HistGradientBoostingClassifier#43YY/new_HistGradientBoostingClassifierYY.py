from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', categorical_features=None, interaction_cst=None, class_weight=None)