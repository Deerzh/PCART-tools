import scipy.stats
a = [1, 2, 2, 3, 3, 3]
skewness = scipy.stats.skew(a=a, axis=0, keepdims=False)