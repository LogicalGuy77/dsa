import sys

s = "hccc"
p = "m*c"

k = p.split("*")
print(k)
len1 = len(k[0])
len2 = len(k[1])

if len2==0 and len1!=0:
    ans = s.find(k[0])
    print("ans=", ans )
    if s.find(k[0]):
        print("true")
        sys.exit(0)

if len1==0 and len2!=0:
    if s.find(k[1]):
        print("true")
        sys.exit(0)

start = s.find(k[0])

if start != -1:
    start += len1 - 1


end = s.find(k[1],start+1)

if end!=-1:
    print(True)
    sys.exit(0)
print(False)
print(end)
