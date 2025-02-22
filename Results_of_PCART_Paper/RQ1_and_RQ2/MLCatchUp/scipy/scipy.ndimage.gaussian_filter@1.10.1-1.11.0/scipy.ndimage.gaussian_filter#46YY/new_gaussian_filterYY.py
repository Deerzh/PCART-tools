from scipy import ndimage
input = ...
sigma = 1.5
order = 0
output = None
mode = 'reflect'
cval = 0.0
truncate = 4.0
radius = None
result = ndimage.gaussian_filter(input, sigma, cval=cval, mode=mode, output=output, radius=radius, order=order, axes=None)
