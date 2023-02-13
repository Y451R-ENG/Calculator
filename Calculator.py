def calculator(num1, num2, operator):
    operations = {
        '+': lambda: num1 + num2,
        '-': lambda: num1 - num2,
        '*': lambda: num1 * num2,
        '/': lambda: num1 / num2
    }
    if operator in operations:
        return operations[operator]()
    else:
        return "Invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print("Result:", result)
