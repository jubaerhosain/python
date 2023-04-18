import numpy as np
import matplotlib.pyplot as plt
import matplotlib

print(matplotlib.__version__)


xpoints = np.arange(40)
ypoints = np.arange(40)

# plt.plot(xpoints, ypoints)
# plt.plot(xpoints, ypoints, 'o')

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)

ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(ypoints, marker = '.')

plt.plot(ypoints, 'o-g',  ms = 5)

plt.show()
