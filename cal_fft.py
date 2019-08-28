#calculate fast fourier transform with scipy.fftpack
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

A=50
freq=10
tup=5
# get t of 200 numbers from 0 to 5
t = np.linspace(0.0, tup, 200)
wave=A * np.cos(2 * np.pi * t*freq)
#wave=A * np.cos(2 * np.pi *t*t)
# the following wave is an example in https://en.wikipedia.org/wiki/Fourier_transform
waves=A * np.cos(6 * np.pi * t)*np.exp(- np.pi*t*t)
#plot wave
fig, ax = plt.subplots()
ax.plot(t, wave)

# Fast Fourier Transform
y_fft = scipy.fftpack.fft(wave)

# plot fft results in frequency dimension
N=100
# get x_fft of 100 numbers from 0 to 20
x_fft = np.linspace(0.0, N/tup, 100)

fig, ax = plt.subplots()
ax.plot(x_fft, 1./N * np.abs(y_fft[:N]))
plt.title('Fast Fourier Transform')
plt.xlabel('frequency')
plt.ylabel('amplitude')
