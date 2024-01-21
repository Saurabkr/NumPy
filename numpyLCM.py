import numpy as np

arrLcm = np.lcm(4,6)
print("LCM of two number is :",arrLcm)

#LCM of more than two numbers:
arr = np.lcm.reduce([2,4,24])
print(arr)

arr1 = np.arange(1,11)
arrLCM1 = np.lcm.reduce(arr1)
print(arrLCM1)

######################################################################################################################

#HCF of two number
arrHCF = np.gcd(3,12)
print(arrHCF)

#HCF of more than 2 numbers

arrHCF1 = np.gcd.reduce([24,68,12,44])
print(arrHCF1)