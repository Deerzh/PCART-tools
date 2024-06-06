from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, 2, return_code=True, callback=None, method='lars', dict_init=None, batch_size=3, alpha=1, n_jobs=None, n_iter=100, shuffle=True, verbose=False, max_iter=None, tol=0.001, max_no_improvement=10)