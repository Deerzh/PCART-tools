from scipy import stats
a = [[1, 2, 2, 4], [3, 2, 4, 1], [1, 2, 3, 1]]
result = stats.mode(a, axis=0, nan_policy='propagate')