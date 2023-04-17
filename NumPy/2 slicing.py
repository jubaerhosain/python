import numpy as np

arr = np.array([6, 7, 8, 9, 10])

print(arr[1:4:2])
print(arr.shape, arr[-3:])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 0:4])
print(arr[0:2, 4])

print(arr[0:2, 2:4])

