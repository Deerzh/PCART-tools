import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.expanding(min_periods=1, center=False, axis=0).sum()