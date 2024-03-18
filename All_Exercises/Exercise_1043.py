# Variavéis
a, b, c = map(float, input().split())

if a + b > c and a + c > b and b + c > a: # Verificação de que, se a soma de dois lados é maior do que o terceiro para que resulte em um triangulo    
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {:.1f}'.format((a + b) * c / 2)) # Caso contrário será um trapézio