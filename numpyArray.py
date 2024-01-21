import numpy as np

zeroDim = np.array(45)
oneDim = np.array([1,4,5,6,2])
twoDim = np.array([[1,6,7],[8,9,3]])
threeDim = np .array([[[2,5,44],[7,93,6]],[[73,5,3],[83,6,34]]])

print(zeroDim)
# To know the type
print(type(zeroDim))
# To know the dimension
print(zeroDim.ndim)

print(oneDim)
print(type(oneDim))
print(oneDim.ndim)

print(twoDim)
print(type(twoDim))
print(twoDim.ndim)

print(threeDim)
print(type(threeDim))
print(threeDim.ndim)

# we can change the dimension of the array
arr = np.array([2,3,5,8,9], ndmin=4)
print(arr)
print(type(arr))
print(arr.ndim)
