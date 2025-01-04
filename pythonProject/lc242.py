import sys

s = "anagram"
t = "nagaram"

# sc = sorted(s)
# sc = ''.join(sc)
#
# tc = sorted(t)
# tc = ''.join(tc)
#
# print(sc, tc)

count = [0]*26

# ord = ascii value
for x in s:
    count[ord(x) - ord('a')] += 1

for x in t:
    count[ord(x) - ord('a')] -= 1

for c in count:
    if c!=0:
        print(False)
        sys.exit(0)

print(True)
