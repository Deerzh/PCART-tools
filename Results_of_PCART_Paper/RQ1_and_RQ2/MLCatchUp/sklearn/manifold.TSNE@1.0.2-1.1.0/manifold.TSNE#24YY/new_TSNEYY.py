import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(random_state=None, verbose=0, learning_rate='warn', metric='euclidean', init='warn', min_grad_norm=1e-07, n_iter_without_progress=300, early_exaggeration=12.0, n_iter=1000, perplexity=30.0).fit_transform(X, metric_params=None)
