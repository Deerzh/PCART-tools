import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', vmin=None, alpha=None, data=None, aspect='auto', interpolation_stage=None)