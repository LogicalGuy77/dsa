s = "   -042"
n = "1234567890"
def atoi(s: str):
    ans = 0
    l = len(s)
    i = 0
    flag = 1
    while i<l and s[i] == " ":
        i+=1

    if i>=l:
        return 0

    if s[i] == '-':
        flag = -1
        i+=1
    elif s[i] == '+':
        i+=1
    while i<l and s[i] in n:
        ans = ans*10 + int(s[i])

        if ans*flag > 2**31-1:
            return 2**31-1
        if ans*flag < -2**31:
            return -2**31
        i+=1
    print(ans*flag)

atoi(s)