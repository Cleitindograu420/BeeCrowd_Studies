x, y = map(int, input().split())
line = 1
for i in range (y):
    line += 1
    if line == x:
        print(i+1, end='\n')
        line = 0
    else:
        print(i+1, end=' ')
    
    '''
    n1,n2 = list(map(int,input().split()))
cont = 1
for i in range(1,(int((n2/n1))+1)):
    r = ""
    for y in range(n1):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])
    '''