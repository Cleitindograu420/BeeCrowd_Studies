# Declaration of variables:
a = int(input())
digit = a
notas = [100,50,20,10,5,2,1]  # list
resto = 0

# Main loop to iterate through the notas
print(digit)
for i in range(len(notas)):
    resto = a // notas[i]
    a %= notas[i]
    print('{} nota(s) de R$ {},00'.format(resto,notas[i]))
    