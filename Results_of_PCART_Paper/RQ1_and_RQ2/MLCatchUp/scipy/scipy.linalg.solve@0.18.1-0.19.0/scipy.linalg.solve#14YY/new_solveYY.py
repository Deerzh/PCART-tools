import scipy.linalg
a = [[3, 2, 0], [1, -1, 0], [0, 5, 1]]
b = [2, 4, -1]
x = scipy.linalg.solve(a, b, False, False, overwrite_a=False, assume_a='gen', transposed=False)