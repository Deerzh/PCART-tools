import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filternorm=True, interpolation='nearest', alpha=None, aspect='auto', interpolation_stage=None)
