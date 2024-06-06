import numpy as np
from sklearn.covariance import GraphicalLassoCV
true_cov = np.array([[0.8, 0.0, 0.2, 0.0], [0.0, 0.4, 0.0, 0.0], [0.2, 0.0, 0.3, 0.1], [0.0, 0.0, 0.1, 0.7]])
np.random.seed(0)
X = np.random.multivariate_normal(mean=[0, 0, 0, 0], cov=true_cov, size=200)
cov = GraphicalLassoCV(alphas=4, n_jobs=None, enet_tol=0.0001, n_refinements=4, tol=0.0001, mode='cd', cv=None, max_iter=100, eps=2.220446049250313e-16)