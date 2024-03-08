# Declaration of variables
x1, y1 = map(float, input().split())  # the function "map()" apply a function to all itens on a list and return an "i" with results.
x2, y2 = map(float, input().split())  # the function "Split()" is a methon that divide one string into substrings

# Calculate
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Result
print("{:.4f}".format(distancia))