import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filterrad=4.0, vmin=None, extent=None, origin='upper', vmax=None, aspect='auto', interpolation='nearest', alpha=None, interpolation_stage=None)