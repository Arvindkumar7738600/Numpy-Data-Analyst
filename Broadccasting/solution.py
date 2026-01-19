import numpy as np

prices = np.array([100, 200, 300, 400])

discount = 10  # 10% discount

final_prices = prices - (prices * discount / 100)
print(final_prices)  # Output: [ 90. 180. 270. 360.]