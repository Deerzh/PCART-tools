import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', alpha=None, resample=None, origin='upper', vmax=None, vmin=None, aspect='auto', interpolation_stage=None)