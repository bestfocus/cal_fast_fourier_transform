import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

A=50
freq=10
# get t of 200 numbers from 0 to 5
t = np.linspace(0.0, 5, 200)
sum_waves=A * np.cos(2 * np.pi * t*freq)
#sum_waves=A * np.cos(2 * np.pi *t*t)
# Fast Fourier Transform
y_fft = scipy.fftpack.fft(sum_waves)

spacing = 5 / 100
# get x_fft of 100 numbers from 0 to 20
x_fft = np.linspace(0.0, 1.0/spacing, 100)
