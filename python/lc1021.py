s = "(()())(())"
stack = []
ans = ""

for c in s:
    if c=="(":
        if len(stack)>0:
            ans+="("
        stack.append(c)
    else:
        k = stack.pop()
        if len(stack)>0:
            ans+=")"

print(ans)
