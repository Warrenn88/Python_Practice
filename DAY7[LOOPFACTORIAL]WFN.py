number = int(input("Input a number for its factorial"))
factorial = 1

for i in range(1,number + 1):
    factorial *= i

print(factorial)