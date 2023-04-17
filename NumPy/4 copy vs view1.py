import numpy as np

# Create a 2D array of shape (2, 3) filled with ones
arr = np.ones((2, 3))

# Create a view of arr with reversed shape
y = arr.view()[::-1]

# Modify the first element of y
y.reshape(1, 6)
# print(y)

# Check the value of arr
# print(arr)
# Output: array([[3., 1., 1.],
#                [1., 1., 1.]])

print(y.base)
