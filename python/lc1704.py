s="textbook"

l = len(s)
a = s[0:(l // 2)]
b = s[l // 2:]
ca, cb = 0, 0
print(a)
print(b)
for i in a:
    if (i in "AEIOUaeiou"):
        ca += 1
for i in b:
    if (i in "AEIOUaeiou"):
        cb += 1
print(ca, cb)