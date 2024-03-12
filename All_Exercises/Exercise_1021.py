# Declaration of variables:
a = float(input())
notas = [100,50,20,10,5,2]  # list
moedas = [1.00,0.50,0.25,0.10,0.05,0.01]
resto = 0

# Main loop to iterate through the notas
print('NOTAS:')
for i in range(len(notas)):
    resto = a // notas[i]
    a %= notas[i]
    print('{:.0f} nota(s) de R$ {}.00'.format(resto,notas[i]))
    
# Main loop to iterate through the coins 
print('MOEDAS:')    
for i in range(len(moedas)):
    a = round(a, 2) # Keeping only two decimal places for accuracy, and use round()
    qt_moedas = int(a / moedas[i])
    print('{} moeda(s) de R$ {:.2f}'.format(qt_moedas, moedas[i]))
    a -= qt_moedas * moedas[i]
