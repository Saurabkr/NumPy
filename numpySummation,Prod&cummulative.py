import numpy as np

# Summation 1 array
arr = np.array([1,2,3,4])
arrNew = np.sum(arr)
print(arrNew)

# Summation 2 array
arr1 = np.array([2,3,4,5])
arrSummation = np.sum([arr,arr1],axis=1)
print(arrSummation)

#cummulative summation 1 array
arrCum = np.cumsum(arr)
print(arrCum) #[1, 1+2, 1+2+3, 1+2+3+4]

############################################################################################################


#prod() 1 array
prodArr = np.array([2,3,4,5])
prodRes = np.prod(prodArr)
print(prodRes)

#prod with 2 array
prodArr2 = np.array([1,2,3,4])
prodRes1 = np.prod([prodArr,prodArr2],axis=1)
print(prodRes1)

#cummulative summation 1 array
prodCum = np.cumprod(prodArr2)
print(prodCum) #[1, 1*2, 1*2*3, 1*2*3*4]

####################################################################################################################

#Difference between array element
arrDiff = np.array([5,25,24,12])
arrResult = np.diff(arrDiff)
print(arrResult) #[25-5, 24-25, 12-24]