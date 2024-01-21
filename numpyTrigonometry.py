import numpy as np

#Sin value
arr = np.sin(np.pi/2)
print(arr)

arr1 = np.array([np.pi/2,np.pi, np.pi/3])
arrRes = np.sin(arr1)
print(arrRes)

#Degree to radian & Radian to Degree
arrDeg = np.deg2rad([90,180,60])
print(arrDeg)

arrRad = np.rad2deg([np.pi/2, np.pi/3, np.pi])
print(arrRad)

#Pass angle as argument
arrAng  = np.arccos(0)
print(arrAng)

#Find hypotenuse 
arrHypo = np.hypot(3,4)
print(arrHypo)