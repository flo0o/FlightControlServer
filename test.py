import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np



x = np.arange(0, 100, 10)
y = np.arange(400, 500, (500-400)/10)
f = interpolate.interp1d(x, y, fill_value='extrapolate')

xnew = 50
ynew = f(xnew)   # use interpolation function returned by `interp1d`
plt.plot(xnew, ynew, 'o')
plt.show()