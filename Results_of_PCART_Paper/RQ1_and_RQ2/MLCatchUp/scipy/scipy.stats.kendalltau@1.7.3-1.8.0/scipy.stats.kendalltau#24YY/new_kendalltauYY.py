import scipy.stats
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
result = scipy.stats.kendalltau(x, y=y, initial_lexsort=True, nan_policy='propagate', method='auto', variant='b', alternative='two-sided')
