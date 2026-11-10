# Signals and Systems: Signal Noise Filtering & LTI System Response Simulator

This project is a Python-based implementation for **Signals and Systems**. It simulates how a Linear Time-Invariant (LTI) system processes a noisy audio signal, designs a digital low-pass filter, and visualizes the results in both Time and Frequency domains.

## 🚀 Features
- **Signal Generation:** Simulates a clean low-frequency audio signal mixed with high-frequency channel noise.
- **LTI System Response:** Designs and applies a 4th-order **Butterworth Low-Pass Filter** using `scipy.signal`.
- **Frequency Domain Analysis:** Uses Fast Fourier Transform (**FFT**) via `numpy.fft` to analyze the magnitude spectrum before and after filtering.
- **Visualization:** Generates dynamic time-domain graphs and frequency spectrum plots using `matplotlib`.

## 🛠️ Tech Stack & Libraries Used
- **Python 3**
- **NumPy** (For mathematical operations and FFT)
- **SciPy** (For digital filter design and LTI simulation)
- **Matplotlib** (For plotting the signal graphs)

## 📊 How it Works
1. The program creates a combined signal of **5 Hz** (Target signal) and **120 Hz** (Noise).
2. A cutoff frequency of **15 Hz** is set for the Butterworth filter.
3. The noise is removed, and the output is plotted to visually show the transition in both time and frequency.
