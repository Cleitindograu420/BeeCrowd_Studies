def media(a,b,c):
    med = (a * 2 + b * 3 + c * 5)/10
    return print('{:.1f}'.format(med))

n = int(input())

for _ in range(0,n):
    a, b, c = map(float, input().split())
    media(a,b,c)
    