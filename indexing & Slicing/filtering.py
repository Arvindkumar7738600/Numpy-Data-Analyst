# filtering means getting elements based on some conditions

import numpy as np
arr = np.array([10, 15, 20, 25, 30])

print(arr[arr > 20])  # Elements greater than 20
print(arr[arr % 2 == 0])  # Even elements