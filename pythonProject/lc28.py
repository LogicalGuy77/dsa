import sys

haystack = "leetcode"
needle = "leeto"

str = ""

for i in range(0, len(haystack)):
    str+=haystack[i]
    if needle in str:
        print(i-len(needle)+1)
        sys.exit(0)


print(-1)