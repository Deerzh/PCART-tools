from scipy import signal
b = [1, 2, 1]
a = [1, -0.5, 0.25]
pairing = 'nearest'
sos = signal.tf2sos(b=b, a=a, pairing=pairing, analog=False)
