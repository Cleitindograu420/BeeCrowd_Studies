# Declaration of variables:
age = int(input()) #  Input age in years
date = [365,30,1]  # List
lista = ['ano(s)','mes(es)','dia(s)']   # List with months in Portuguese
div = 0 # Division of integers

# Main loop to iterate through dates
for i in range(len(date)):
    div = age // date[i]
    age %= date[i]
    print('{} {}'.format(div, lista[i]))
    