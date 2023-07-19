# python code to read input and multiply it by another input without comments

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The result of {num1} multiplied by {num2} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")