def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication

x, y, z = calculate(10, 5)

print("Addition =", x)
print("Subtraction =", y)
print("Multiplication =", z)