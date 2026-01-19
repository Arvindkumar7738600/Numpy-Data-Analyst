price = [100, 200, 300]

discount = 10  # 10% discount

final_price = []

for price in price:
    discounted_price = price - (price * discount / 100)
    final_price.append(discounted_price)

print(final_price)  # Output: [90.0, 180.0, 270.0]