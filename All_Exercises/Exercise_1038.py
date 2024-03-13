# Declaration of variables
u_cod, qnt = map(int,input().split())

# Lists of products code and price
cod = [1,2,3,4,5]
preco = [4.00,4.5,5,2,1.50]
tot = 0

for i in cod:
    if u_cod == i:
        tot += preco[i-1] * qnt
        print('Total: R$ {:.2f}'.format(tot))
