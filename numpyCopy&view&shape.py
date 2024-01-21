import numpy as np

arr = np.array([2,4,6,7,8])
#copy an array
arrcpy = arr.copy()
#change made in original array after copy is done does not impact copied array
arr[0] = 9

print('original arr:', arr)
print('Copied array:',arrcpy)
print('Shaape of Array:', arr.shape)

#If we change the value in copied array then original is untouched
arrcpy[0]=12
print('original arr after change:', arr)
print('Copied array after change:',arrcpy)

#view function 
arrView = arr.view()

print('original arr:', arr)
print('view array:',arrView)
print('Shape of Array:', arr.shape)

#Shape of an array
arr2 = np.array([[4,6,7],[8,9,5]])
arr3 = np.array([[[4,6,4],[7,9,8]],[[4,6,1],[7,9,9]]])
print('Shape of array:',arr2.shape)
print('Shape of array:',arr3.shape)
