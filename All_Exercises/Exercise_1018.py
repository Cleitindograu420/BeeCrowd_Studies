# Declaration   of the class for the main window
a, b, c = map(int, input().split())

# If clause
if a > b:
    maior = a
else:
    maior = b

if c > maior:
    maior = c

# Printing the result
print(maior, "eh o maior")