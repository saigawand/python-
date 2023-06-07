import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")

# Saving the program to a file
filename = "factorial.py"
with open(filename, "w") as file:
    file.write("""import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
""")
print(f"The program has been saved to {filename}")
