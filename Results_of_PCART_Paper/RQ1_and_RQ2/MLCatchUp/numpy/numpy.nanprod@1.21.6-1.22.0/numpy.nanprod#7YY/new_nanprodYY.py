import numpy as np
result = np.nanprod([1, 2, np.nan, 4],  0, dtype=int)
