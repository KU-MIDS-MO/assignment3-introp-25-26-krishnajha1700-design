import numpy as np

def moving_average(signal, window_size):
   
    if window_size % 2 == 0 or window_size < 1:
        raise ValueError("window_size must be a positive odd integer")

    n = len(signal)
    k = (window_size - 1) // 2
    result = np.empty(n, dtype=float)

    for i in range(n):
        start = max(0, i - k)
        end = min(n - 1, i + k)
        result[i] = np.mean(signal[start:end+1])

    return result