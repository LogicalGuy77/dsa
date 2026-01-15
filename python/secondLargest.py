arr = [12,35,1,10,34,1]
lar, slar = -1, -1

for i in range (0, len(arr)):
    if arr[i]>lar:
        temp = lar
        lar = arr[i]
        slar = temp
    if arr[i]>slar and arr[i]!=lar:
        slar=arr[i]

print(slar, lar)