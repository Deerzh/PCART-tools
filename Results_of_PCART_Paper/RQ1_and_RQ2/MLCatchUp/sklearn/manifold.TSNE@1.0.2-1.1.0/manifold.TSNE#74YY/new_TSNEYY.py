import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(early_exaggeration=12.0, learning_rate='warn', n_components=2, perplexity=30.0, n_iter=1000).fit_transform(X, metric_params=None)
