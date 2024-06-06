from sklearn.cluster import SpectralCoclustering
import numpy as np
X = np.array([[1, 1], [2, 1], [1, 0], [4, 7], [3, 5], [3, 6]])
clustering = SpectralCoclustering(2, n_svd_vecs=None, mini_batch=False, init='k-means++', svd_method='randomized').fit(X)