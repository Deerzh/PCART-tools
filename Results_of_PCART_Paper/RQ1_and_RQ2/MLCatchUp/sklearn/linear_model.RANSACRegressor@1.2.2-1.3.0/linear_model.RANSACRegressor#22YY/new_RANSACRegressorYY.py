from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(max_trials=100, max_skips=0, stop_score=0, loss='absolute_error', stop_n_inliers=0, residual_threshold=None, min_samples=None, is_model_valid=None, is_data_valid=None, stop_probability=0.99)