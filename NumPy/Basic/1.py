import numpy as np

array = np.array([1, 2, 3, 4])

print(type(array))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=4)

print(arr)
print('number of dimensions :', arr.ndim)