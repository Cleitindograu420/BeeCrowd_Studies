positivo = 0 
negativo = 0 
par = 0
impar = 0


for i in range (0,5):
    num = int(input())
    if num > 0:
        positivo += 1
        if num % 2 == 0 or num == 0:
            par += 1
        else:
            impar += 1
    elif num < 0:
        negativo += 1
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
            print(i) 
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(par,impar,positivo,negativo))
