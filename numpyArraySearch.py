import numpy as np

arr = np.array([2,3,4,5,6,7])
arrSearch = np.where(arr==6)
#print index of element 6
print(arrSearch)

#print indexes of element which is even
arrSearchEven = np.where(arr%2==0)
print(arrSearchEven)

#searchsorted : use to perform binary search in array
arr1 = np.array([1,2,3,4,5,6,7,8,9])
arrSrch = np.searchsorted(arr1, 6) #search from left
arrSrch1 = np.searchsorted(arr1, 6, side='right') #search from right
print(arrSrch)
print(arrSrch1)

#Multiple search
arrMul = np.array([1,3,5,7])
arrSearchMul = np.searchsorted(arrMul,[2,4,6])
print(arrSearchMul)
