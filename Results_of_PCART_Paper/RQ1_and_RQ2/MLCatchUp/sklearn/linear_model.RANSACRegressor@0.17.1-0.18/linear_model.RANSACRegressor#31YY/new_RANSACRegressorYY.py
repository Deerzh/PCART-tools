from sklearn.linear_model import RANSACRegressor
reg = RANSACRegressor(None, None, None, None, None, max_trials=100, stop_n_inliers=0, loss='absolute_loss')