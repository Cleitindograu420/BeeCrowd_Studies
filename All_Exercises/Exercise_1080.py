maior = 0
for i in range (1,101):
    n = int(input())
    if n > maior:
        ct = i
    maior = max(n,maior)
print(maior)
print(ct)
