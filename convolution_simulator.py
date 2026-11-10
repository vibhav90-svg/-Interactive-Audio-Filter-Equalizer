import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Generate a synthetic noisy signal (Simulating audio)
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1.0, fs, endpoint=False)  # 1 second duration
clean_signal = np.sin(2 * np.pi * 5 * t)  # 5 Hz target signal
noise = np.sin(2 * np.pi * 120 * t) + 0.5 * np.random.normal(size=t.shape)  # High-frequency noise
noisy_signal = clean_signal + noise

# 2. Design a Low-Pass Butterworth Filter
cutoff = 15  # Cutoff frequency (Hz)
nyquist = 0.5 * fs
normal_cutoff = cutoff / nyquist
b, a = signal.butter(N=4, Wn=normal_cutoff, btype='low', analog=False)

# 3. Apply the filter (LTI System Response)
filtered_signal = signal.lfilter(b, a, noisy_signal)

# 4. Plotting the results
plt.figure(figsize=(12, 6))

# Time Domain Plot
plt.subplot(2, 1, 1)
plt.plot(t, noisy_signal, label='Noisy Signal', color='orange', alpha=0.7)
plt.plot(t, filtered_signal, label='Filtered (Cleaned) Signal', color='blue', linewidth=2)
plt.title('Time Domain: Audio Filtering')
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Frequency Domain Plot (Magnitude Spectrum via FFT)
plt.subplot(2, 1, 2)
freqs = np.fft.rfftfreq(len(t), 1/fs)
fft_noisy = np.abs(np.fft.rfft(noisy_signal))      # <-- Fixed here
fft_filtered = np.abs(np.fft.rfft(filtered_signal))  # <-- Fixed here

plt.plot(freqs, fft_noisy, label='Noisy Spectrum', color='orange', alpha=0.7)
plt.plot(freqs, fft_filtered, label='Filtered Spectrum', color='blue')
plt.title('Frequency Domain: Signal Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.xlim(0, 200)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

