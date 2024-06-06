from sklearn.cluster import AffinityPropagation
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
clustering = AffinityPropagation(copy=True, preference=None, damping=0.5, max_iter=200, convergence_iter=15).fit(damping=X, random_state='warn')