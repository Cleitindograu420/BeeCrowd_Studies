ct = 0
for i in range (0,5):
    num = int(input())
    if num%2 == 0:
        ct += 1
        print(i) # Do not print on your beecrowd
print('{} valores pares'.format(ct))

