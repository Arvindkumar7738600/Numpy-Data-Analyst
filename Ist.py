temperature = [34.2, 36.5, 33.1, 35.0, 37.8]

total = 0
for temp in temperature:
    total += temp

average = total / len(temperature)
print(average)