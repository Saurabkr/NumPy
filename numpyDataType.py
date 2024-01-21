import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

#Throw error becuse we cannot convert 'a' to int
'''str = np.array(['a','2','3','4'], dtype='i')
print(str)'''

#int -> string
arr1 = np.array([1,2,3,4], dtype='S')
print(arr1)

#converting integer to boolean
arr2 = np.array([1,4,0,3,0])
boolArr2 = arr2.astype(bool) 
print(boolArr2)

#converting float to int
arr3 = np.array([1.3,4.4,3.5])
intArr3 = arr3.astype('i') 
print(intArr3)

#converting int to float
arr4 = np.array([1,3,4,4,3,5])
fArr4 = arr4.astype('f') 
print(fArr4)





