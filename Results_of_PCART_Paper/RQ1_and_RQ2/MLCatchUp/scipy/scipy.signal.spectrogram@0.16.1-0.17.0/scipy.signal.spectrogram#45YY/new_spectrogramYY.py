import numpy as np
from scipy.signal import spectrogram
x = np.random.randn(5)
fs = 8000
nperseg = len(x)
noverlap = nperseg // 2
nfft = nperseg
axis = -1
(f, t, Sxx) = spectrogram(x=x, fs=fs, window=('tukey', 0.25), nperseg=nperseg, noverlap=noverlap, nfft=nfft, detrend='constant', return_onesided=True, scaling='density', mode='psd')