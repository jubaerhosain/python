import numpy as np

arr = np.array([6, 7, 8, 9, 10])

print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i1')
arr = np.array([1, 2, 3, 4333], dtype='i4')

print(arr[3])
print(arr.dtype)


arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)
print(newarr)

print(newarr.dtype)
