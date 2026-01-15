n=2
arr =[8,9]
p=5

def res(arr, p, n):
    hashArr = [0]*n

    for i in range(0, n):
        ele = arr[i]
        if ele<=n:
            hashArr[ele-1]+=1
    for i in range(0, n):
        arr[i] = hashArr[i]

    print(arr)

res(arr,p,n)