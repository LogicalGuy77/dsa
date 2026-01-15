s = "a good   example"

ans = " ".join(s.split())

ans = " ".join(ans.split()[::-1])
print(ans)