num1 = float(input("Please enter first number: "))
num2 = float(input("Please enter second number: "))
operation = input("Please enter an operation (+, -, *, /): ")

if operation == "+":
    print(f"Result = {num1 + num2}")
elif operation == "-":
    print(f"Result = {num1 - num2}")
elif operation == "*":
    print(f"Result = {num1 * num2}")
elif operation == "/":
    print(f"Result = {num1 / num2}")
else:
    print("Invalid operation")
