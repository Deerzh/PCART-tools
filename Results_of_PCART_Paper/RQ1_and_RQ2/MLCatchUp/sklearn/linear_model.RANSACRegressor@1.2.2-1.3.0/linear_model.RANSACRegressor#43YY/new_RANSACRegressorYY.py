from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(None, residual_threshold=None, is_model_valid=None, max_trials=100, min_samples=None, is_data_valid=None, max_skips=0, stop_n_inliers=0)
