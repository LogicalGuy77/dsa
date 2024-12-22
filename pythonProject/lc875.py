import math

piles = [3, 6, 7, 11]
h = 8
ans = 0
low = 1
high = max(piles)

while low <= high:
    mid = (low + high) // 2

    t = time(piles, k)

    if t <= h:
        ans = t
        high = mid - 1
    else:
        low = mid + 1
print(ans)


def time(self, pile, k):
    ti = 0
    for i in pile:
        ti += math.ceil(i / k)
    return ti
