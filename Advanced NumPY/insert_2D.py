import numpy as np

arr_2d = np.array([[1, 2],[4, 5]])
print(arr_2d)

new_arr = np.insert(arr_2d, 1, [10, 20], axis=0)
print(new_arr) #output after inserting a new row at index 1


#diffrence btw axis 0 and 1
new_arr = np.insert(arr_2d, 1, [10, 20], axis=1)
print(new_arr) 

# axis=None   means flatten the array before inserting
new_arr = np.insert(arr_2d, 1, [10, 20], axis=None)
print(new_arr) 