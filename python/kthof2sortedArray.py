import sys

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

k-=1
n1 = len(a)
n2 = len(b)
p1, p2 = 0, 0
ctr = 0
while p1<n1 and p2<n2:
    if a[p1]<b[p2]:
        if ctr == k:
            print(a[p1])
            sys.exit(1)
        p1+=1
        ctr+=1

    else:
        if ctr == k:
            print(b[p2])
            sys.exit(1)
        p2+=1
        ctr+=1

while p1<n1:
    if ctr == k:
        print(a[p1])
        sys.exit(1)
    p1+=1
    ctr+=1

while p2<n2:
    if ctr == k:
        print(b[p2])
        sys.exit(1)
    p2+=1
    ctr+=1
