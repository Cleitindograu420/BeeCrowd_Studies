# Read the information
cod_1, num_1, valor_1 = map(float, input().split())
cod_2, num_2, valor_2 = map(float, input().split())

# Calcular o valor total a ser pago
total = (num_1 * valor_1) + (num_2 * valor_2)

# Print the formated result
print("VALOR A PAGAR: R$ {:.2f}".format(total))
