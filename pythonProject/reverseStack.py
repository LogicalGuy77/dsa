St = [4, 3, 9, 6]


def addToBottom(stack, ele):
    if not stack:
        stack.append(ele)
        return
    top = stack.pop()
    addToBottom(stack, ele)
    stack.append(top)


def reverse(stack):
    if not stack:
        return
    top = stack.pop()
    reverse(stack)

    addToBottom(stack, top)

print(St)
reverse(St)
print(St)
