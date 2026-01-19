'''
np.concatenate((aray1, array2, ...) axis=0) 

axix=0  means vertical concatenation (along rows)
axis=1  means horizontal concatenation (along columns)
'''
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

new_arr = np.concatenate((arr1, arr2))
print(new_arr) #output: [1 2 3 4 5 6]