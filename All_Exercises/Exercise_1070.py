
num = int(input())
ct = 0
if num %2 == 0:
    num += 1
    print(num)
    ct = ct + 1
else:
    print(num)
    ct = ct + 1
while ct < 6:
    num += 2
    print(num)
    ct = ct + 1

