n = int(input())
into = 0
out = 0
for  i in range(0,n):
    x = int(input())
    if 10 <= x and x <= 20:
        into += 1
    else:
        out += 1
print('{} in\n{} out'.format(into,out))