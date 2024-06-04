
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))
n3 = int(input("Enter the third integer: "))

mean = (n1+n2+n3)/3

print(mean)

message = "The mean is {mean}"
print(message.format(mean = mean))

message = "The mean is {mean:.3f}"
print(message.format(mean = mean))
