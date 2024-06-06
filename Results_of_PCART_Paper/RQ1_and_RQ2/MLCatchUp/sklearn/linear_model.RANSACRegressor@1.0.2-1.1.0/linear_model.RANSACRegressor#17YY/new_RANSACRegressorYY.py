from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(max_trials=100, residual_threshold=None, is_model_valid=None, max_skips=np.inf, min_samples=None, is_data_valid=None, estimator=None)