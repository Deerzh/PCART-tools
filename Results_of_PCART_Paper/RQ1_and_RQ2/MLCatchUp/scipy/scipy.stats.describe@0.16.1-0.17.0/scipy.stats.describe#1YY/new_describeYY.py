from scipy import stats
a = [[1, 2, 3], [4, 5, 6]]
result = stats.describe(a, bias=True, nan_policy='propagate')
