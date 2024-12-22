s = "bcbbbcba"
sublen=0
freq = {}

for i in range(len(s)):
    sublen+=1
    if s[i] in freq:
        freq[s[i]]+=1
    else:
        freq[s[i]]=1
    if freq.get(s[i])>2:
        break
print(freq, sublen-1)
