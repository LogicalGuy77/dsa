arr = [1, 3, 3]
n = len(arr)

sf = (n*(n+1))//2
sf2 = (n*(n+1)*(2*n+1))//6

sa = sum(arr)
sa2 = sum(x*x for x in arr)

aminusb = sf - sa
aplusb = (sf2 - sa2)//aminusb

a = (aminusb + aplusb)//2
b = aplusb - a

print([b,a])