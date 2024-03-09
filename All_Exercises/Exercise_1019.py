# Declaration of Variable
n = int(input())

# Calculate hours, minutes and seconds
hour = n // 3600
n %= 3600
minutes = n // 60
n %= 60

# Print the time  in the format HH:MM:SS
print("{:1d}:{:1d}:{:1d}".format(hour, minutes, n))