a, b = map(int, input().split())


if b%a == 0 or a%b == 0: # See if the variables are or not multiple
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')