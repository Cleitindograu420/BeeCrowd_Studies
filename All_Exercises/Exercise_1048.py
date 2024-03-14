# Declaration of variables
a = float(input())
b = a

# If clauses  to check if the input is positive or negative and apply o increase
if a > 0 and a <= 400:
    b = a * 1.15
elif a > 400 and a <= 800:
    b = a * 1.12
elif a > 800 and a <= 1200:
    b = a * 1.10
elif a > 1200 and a <= 2000:
    b = a * 1.07
elif a > 2000:
    b = a * 1.04
percentual = ((round(b)/a) * 100) - 100
gain = b - a

# Result Printed
print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'.format(b,gain,percentual))