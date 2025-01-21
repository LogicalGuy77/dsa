s = [2, 3, 1]
s1 = []
s2 = []

while s:
    if not s1:
        s1.append(s.pop())
        continue
    if s1[-1] < s[-1]:
        s1.append(s.pop())
    else:
        while s1 and s1[-1]>s[-1]:
            s2.append(s1.pop())
        s1.append(s.pop())
        while s2:
            s1.append(s2.pop())
for i in s1:
    s.append(i)

print(s)