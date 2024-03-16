num = int(input())
ct = 0
while ct < 6:
    if num %2 == 0:
        num += 1
        print(num)
        ct = ct + 1
    else:
        num += 2
        print(num)
        ct = ct + 1
    