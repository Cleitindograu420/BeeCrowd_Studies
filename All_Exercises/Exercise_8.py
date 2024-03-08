# Declaration of Variables
time = int(input())
speed = int(input())

# Calculate
distance = time * speed
consumption = distance / 12

# Result
print("{:.3f}".format(consumption))