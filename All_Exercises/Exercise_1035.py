# Declaration of variables
a, b, c, d = map(int, input().split())

# Calculation and assignment of the result variable
if b > c and d > a and c + d > b + a and a%2 == 0:
    print("Valores aceitos")
    
else:
    print("Valores nao aceitos")
    