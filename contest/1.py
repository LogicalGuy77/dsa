num =112

if num == 0:
    print(0)
SystemExit(0)
pro = 1
while num > 0:
    pro = pro * (num % 10)
    num = num // 10

print(pro)