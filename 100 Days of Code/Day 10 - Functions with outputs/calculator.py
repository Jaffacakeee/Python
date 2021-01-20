from art import logo
# Add
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculater():
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)

    should_contine = True
    while should_contine:
        operation_symbol = input("Pick a operation: ")
        num2 = float(input("Enter another number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation. ") == "y":
            num1 = answer
        else:
            print(logo)
            should_contine = False
            calculater()
calculater()
