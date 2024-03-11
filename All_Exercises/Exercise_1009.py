# Declaration of variables
name = input()
salary = float(input())
sales = float(input())

# Calculate the comission and the final salary.
commission = sales * 0.15
finalSalary = salary + commission

# Show the information formatted.
print('TOTAL = R$ {:.2f}'.format(finalSalary))