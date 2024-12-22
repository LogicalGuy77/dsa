x=1534236469
num=0
flag=1
if(x<0) :
    flag=-1
    x=x*-1
while x>0:
    num = num*10 + x%10
    x = x//10
print(num*flag)