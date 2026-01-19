import numpy as np

matrix = np.array([[10, 20, 30], [40, 50, 60]]) #2*3 matrix
vector = np.array([1, 2, 3]) # 1D array

result = matrix + vector  # Broadcasting addition
print(result)