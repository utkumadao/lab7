import math_utils

if __name__ == "__main__":
    print("Simple calculation machine")
    print("Operations: +  -  *  /  **  %")

    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))
        operator = input("Operation (+, -, *, /, **, %): ")

        if operator == "+":
            result = math_utils.add(x, y)
        elif operator == "-":
            result = math_utils.subtract(x, y)
        elif operator == "*":
            result = math_utils.multiply(x, y)
        elif operator == "/":
            result = math_utils.divide(x, y)
        elif operator == "**":
            result = math_utils.power(x, y)
        elif operator == "%":
            result = math_utils.mod(x, y)
        else:
            result = "Invalid operation."

        print("Result:", result)

    except ValueError:
        print("Error. Please enter a number")
