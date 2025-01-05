from collections import Counter
from collections import defaultdict
s = "tree"

count = Counter(s)
buckets = defaultdict(list)

for char, cnt in count.items():
    buckets[cnt].append(char)

res = ""

for i in range(len(s), 0, -1):
    for letter in buckets[i]:
        res += letter * i
print(res)