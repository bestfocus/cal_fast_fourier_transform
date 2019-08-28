#calculate fast fourier transform with scipy.fftpack
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

A=50
freq=10

# get x of 200 numbers from 0 to upper bound xup=5
xup=5
x = np.linspace(0.0, xup, 200)
wave=A * np.cos(2 * np.pi * x *freq)
#wave=A * np.cos(2 * np.pi * x * x)
# the following wave is an example in https://en.wikipedia.org/wiki/Fourier_transform
waves=A * np.cos(6 * np.pi * x)*np.exp(- np.pi*x*x)
#plot wave
fig, ax = plt.subplots()
ax.plot(x, wave)

# Fast Fourier Transform
y_fft = scipy.fftpack.fft(wave)

# plot fft results in frequency dimension
N=100
# get x_fft of 100 numbers from 0 to 20
x_fft = np.linspace(0.0, N/xup, 100)

fig, ax = plt.subplots()
ax.plot(x_fft, 1./N * np.abs(y_fft[:N]))
plt.title('Fast Fourier Transform')
plt.xlabel('frequency')
plt.ylabel('amplitude')
