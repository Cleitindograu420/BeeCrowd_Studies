valor = float(input())
imposto = 0

if valor < 2000:
    print('Isento')
elif valor < 3000:
    valor -= 2000 # pois 2000 reais são Isentos
    imposto = valor * 0.08 # taxa do valor entre 2 a 3 mil
    print('R$ {:.2f}'.format(imposto))
elif valor < 4500:
    valor -= 3000 # 2 mil isentos mais taxa cheia de 8%
    imposto += 80 # Taxa cheia dos 8%
    imposto += valor * 0.18 # Taxa de 18%  a cima de 3 mil reais
    print('R$ {:.2f}'.format(imposto))
elif valor >= 4500:
    valor -= 4500
    imposto =+ valor * 0.28
    imposto += 350
    print('R$ {:.2f}'.format(imposto))
    