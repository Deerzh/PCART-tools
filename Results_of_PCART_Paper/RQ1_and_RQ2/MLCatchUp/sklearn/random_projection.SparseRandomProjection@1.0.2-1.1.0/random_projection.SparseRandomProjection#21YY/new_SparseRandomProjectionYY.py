import numpy as np
from sklearn.random_projection import SparseRandomProjection
rng = np.random.RandomState(42)
X = rng.rand(25, 3000)
transformer = SparseRandomProjection(n_components='auto', random_state=rng, compute_inverse_components=False)
