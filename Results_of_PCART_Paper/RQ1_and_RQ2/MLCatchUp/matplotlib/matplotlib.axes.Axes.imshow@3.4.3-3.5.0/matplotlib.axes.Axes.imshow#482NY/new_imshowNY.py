import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, origin='upper', vmax=None, filternorm=True, alpha=None, vmin=None, aspect='auto', interpolation='nearest', interpolation_stage=None)
