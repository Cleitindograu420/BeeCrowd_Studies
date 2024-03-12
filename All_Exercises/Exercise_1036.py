# Declaration of variables
a, b, c = map(float, input().split())

#  Calculation of delta
delta = ((b**2)-4*a*c)

if( (delta < 0) or a == 0):
	print( "Impossivel calcular")
	
elif ( delta == 0 ):
	radius1 = (-b + delta **(1/2))/(2*a)
	radius2 = radius1
	print("R1 = %.5f" %(radius1))
	print("R2 = %.5f" %(radius2))

else:
	radius1 = (-b + delta **(1/2))/(2*a)
	radius2 = (-b - delta **(1/2))/(2*a)
	print("R1 = %.5f" %(radius1))
	print("R2 = %.5f" %(radius2))
 