inicial, final = map(int,input().split())
resultado = 0
if inicial == final:
    print('O JOGO DUROU 24 HORA(S)')
elif inicial > final:
    resultado = 24 - inicial
    resultado += final
    print('O JOGO DUROU {} HORA(S)'.format(resultado))
elif final > inicial:
    resultado = final - inicial
    print('O JOGO DUROU {} HORA(S)'.format(resultado))
    