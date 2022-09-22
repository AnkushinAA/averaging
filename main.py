import numpy as np
import matplotlib.pyplot as plt


def averagingSignal(arr):
    result = np.zeros(len(arr))
    for i in range(len(arr)):
        if i < 10:
            result[i] = sum(arr[0:i + 1]) / (i + 1)
        else:
            result[i] = sum(arr[i - 9:i + 1]) / 10
    return result


fileNameSignal1 = 'signals/signal01.dat'
fileNameSignal2 = 'signals/signal02.dat'
fileNameSignal3 = 'signals/signal03.dat'
x = input('выберите сигнал 1-3')
if (x == '1'):
    ar = np.loadtxt(fileNameSignal1, float)
if (x == '2'):
    ar = np.loadtxt(fileNameSignal2, float)
if (x == '3'):
    ar = np.loadtxt(fileNameSignal3, float)
arr = np.array(ar)
plt.plot(arr)
plt.plot(averagingSignal(arr))
plt.show()
