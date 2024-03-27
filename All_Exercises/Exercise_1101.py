def sum_sequencial(m, n):
    return sum(range(menor, maior + 1))

while True:
    n, m = map(int,input().split())
    if n <= 0 or m <=0:
        break
    else:
        menor = min(m,n)
        maior = max(m,n)
        sum_sequencial(m,n)
        sequencia = ' '.join(map(str, range(menor, maior + 1)))
    print('{} Sum={}'.format(sequencia,sum_sequencial(m,n)))
