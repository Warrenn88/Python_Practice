import sympy
def prime_checker(n):
    return sympy.isprime(n)

while True:
    n = int(input("Please select a number 1-100\nto check if it is prime."))
    if 0 <= n <= 100:
        print(prime_checker(n))
        break
    else:
        print("Not a valid input, try again")





