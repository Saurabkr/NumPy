import numpy as np

def myAdd(a,b):
    return a+b

#make the function ufunc
myFunc = np.frompyfunc(myAdd,2,1) # 2 -> pass two array and 1-> get one output
print(myFunc([2,3,4],[2,4,6]))
print(type(myFunc))
print(type(myAdd))

#Important unfunc

arr1 = np.array([2,3,4,5,6])
arr2 = np.array([2,3,1,4,2])

arrAdd = np.add(arr1,arr2)
print("Addition",arrAdd)
arrSub = np.subtract(arr1,arr2)
print("Substraction",arrSub)
arrMul = np.multiply(arr1,arr2)
print("Multiplication",arrMul)
arrDiv = np.divide(arr1,arr2)
print("Division",arrDiv)
arrModulus = np.mod(arr1,arr2)
print("Modulus",arrModulus)
arrRem = np.remainder(arr1,arr2)
print("Remainder",arrRem)
arrPow = np.power(arr1,arr2)
print("Power",arrPow)
arrDivMod = np.divmod(arr1,arr2)
print("Quotient and Remaider",arrDivMod)

