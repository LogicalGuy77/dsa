s = "bcbbbcba"
ans=0

for j in range (len(s)):
    freq={}
    sublen=0
    for i in range(j,len(s)):
        sublen+=1
        if s[i] in freq:
          freq[s[i]] += 1
        else:
          freq[s[i]] = 1
        if freq.get(s[i]) > 2:
          sublen-=1
          break
    if sublen>ans:
      ans=sublen
print(ans)