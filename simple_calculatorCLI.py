def mycalculator():
    number1 = float(input("Enter the first number: "))
    operation = input("Choose the following operation (+, -, *, /): ")
    number2 = float(input("Enter the second number: "))

    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        if number2 != 0:
            result = number1 / number2
        else:
            return "Error ,Can not divide by 0"
    else:
        return "Invalid operation"

    return f"The result is: {result}"


print(mycalculator())
