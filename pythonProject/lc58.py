s = "hello world"

words = s.split()

l = len(words)
if l == 1:
    print(len(words[0]))

print(len(words[l-1]))