tot = 0
positive = 0
for i in range(0,6):
    num = float(input())
    if num > 0:
        positive += 1
        i  += 1
        tot += num
    else:
        i += 1
media = tot/positive
print('{} valores positivos\n{:.1f}'.format(positive,media)) 
