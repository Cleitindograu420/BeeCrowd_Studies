"""Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos."""
# Declaration of variables
a, b, c = map(int, input().split())
list = [a, b, c] #List
# Sorted Function to order the  numbers in ascending order.
def  sort(x):
    return sorted(x)

for i in range(3):
    print(sort(list)[i])    
print()
for i in range(3):
    print(list[i])
