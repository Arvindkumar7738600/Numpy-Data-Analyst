#Error kab ayega!

import numpy as np

arr1 = np.array([1, 2, 3], [4, 5, 6])
arr2 = np.array([1, 2]) #mismatch in shape

result = arr1 + arr2  # This will raise a ValueError due to shape mismatch
print(result)