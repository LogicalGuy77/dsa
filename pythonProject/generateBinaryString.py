def getStringsUtil(k, str, n):
    if k==n:
        print(str)
        return
    if str[n-1] == 0:
        str[n] = 0
        getStringsUtil(k, str, n+1)
        str[n] = 1
        getStringsUtil(k, str, n+1)

    if str[n-1] == 1:
        str[n] = 0
        getStringsUtil(k, str, n+1)


def getAllStrings(k):

    if k<=0:
        return

    str = [0]*k

    str[0] = 0
    getStringsUtil(k, str, 1)
    str[0] = 1
    getStringsUtil(k, str, 1)


k = 3
getAllStrings(k)