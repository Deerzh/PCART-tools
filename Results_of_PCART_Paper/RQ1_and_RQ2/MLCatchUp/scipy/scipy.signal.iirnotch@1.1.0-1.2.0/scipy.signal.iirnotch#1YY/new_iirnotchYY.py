import scipy.signal
(w0, Q) = (0.1, 10.0)
(b, a) = scipy.signal.iirnotch(w0, Q, fs=2.0)