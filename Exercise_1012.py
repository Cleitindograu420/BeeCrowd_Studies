# Declaration of variables
a = float(input())
b = float(input())
c = float(input())
pi = 3.14159

# The requested calculation of the question in order
triangulo = (a * c)/2
circulo = pi * c**2
trapezio = ((a+b)*c)/2
quadrado = b * b
retangulo = a * b

# The results in order
print('TRIANGULO = {:.3f}'.format(triangulo))
print('CIRCULO = {:.3f}'.format(circulo))
print('TRAPEZIO = {:.3f}'.format(trapezio))
print('QUADRADO = {:.3f}'.format(quadrado))
print('RETANGULO = {:.3f}'.format(retangulo))
