prices = [2,4,1]
n = len(prices)
max = prices[0]
min = prices[0]
profit = 0

for i in range(1, n):
    if prices[i] < min:
        min = prices[i]
        max = prices[i]
        if (max - min) > profit:
            profit = max - min
        continue
    if prices[i] > max:
        max = prices[i]
        profit = max - min
        continue

print(profit)