from sklearn import linear_model
reg = linear_model.LassoLars(alpha=1.0, fit_intercept=True, verbose=False, normalize=True, jitter=None, random_state=None)