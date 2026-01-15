s = "0P"
good_char = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in s:
    if i not in good_char:
        s = s.replace(i, "")

old = s.lower()
new = old[::-1]

if old == new:
    print(True)
else :
    print(False)

