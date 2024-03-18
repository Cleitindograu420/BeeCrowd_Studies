'''se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES'''


a, b, c = map(float, input() .split())
lista = [a,b,c]
lista.sort(reverse=True)
if lista[0] >= (lista[1]+lista[2]):
    print('NAO FORMA TRIANGULO')
else:
    if lista[0]**2 == (lista[1]**2+lista[2]**2):
        print('TRIANGULO RETANGULO')
    if  lista[0]**2 > (lista[1]**2+lista[2]**2):
        print('TRIANGULO OBTUSANGULO')
    if   lista[0]**2 < (lista[1]**2+lista[2]**2):
        print('TRIANGULO ACUTANGULO')
    if lista[0]==lista[1] and lista[0]==lista[2]:
        print('TRIANGULO EQUILATERO')
    elif  lista[0]==lista[1] or lista[0]==lista[2] or lista[1] == lista[2]:
        print('TRIANGULO ISOSCELES')
