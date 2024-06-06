from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
clustering = AgglomerativeClustering(connectivity=None, n_clusters=2, memory=None, affinity='euclidean').fit(X, compute_distances=False)