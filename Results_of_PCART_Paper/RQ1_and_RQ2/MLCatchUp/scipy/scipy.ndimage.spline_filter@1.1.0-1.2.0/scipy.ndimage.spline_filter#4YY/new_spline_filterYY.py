from scipy.ndimage import spline_filter
input_data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
result = spline_filter(input_data, order=3, mode='mirror')