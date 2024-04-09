def addition(num1, num2):
    """
    Function to perform addition of two numbers.

    Parameters:
    num1 (int/float): First number.
    num2 (int/float): Second number.

    Returns:
    int/float: Sum of num1 and num2.
    """
    return num1 + num2

def subtraction(num1, num2):
    """
    Function to perform subtraction of two numbers.

    Parameters:
    num1 (int/float): First number.
    num2 (int/float): Second number.

    Returns:
    int/float: Result of num1 minus num2.
    """
    return num1 - num2

def multiplication(num1, num2):
    """
    Function to perform multiplication of two numbers.

    Parameters:
    num1 (int/float): First number.
    num2 (int/float): Second number.

    Returns:
    int/float: Product of num1 and num2.
    """
    return num1 * num2

def division(num1, num2):
    """
    Function to perform division of two numbers.

    Parameters:
    num1 (int/float): Dividend.
    num2 (int/float): Divisor.

    Returns:
    int/float: Result of num1 divided by num2.
    """
    if num2 != 0:
        return num1 / num2
    else:
        print("Cannot perform operation")

# Main program
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Select operation +, -, *, /")
c = str(input())

if c == "+":
    print(addition(num1=a, num2=b))
elif c == "-":
    print(subtraction(num1=a, num2=b))
elif c == "*":
    print(multiplication(num1=a, num2=b))
elif c == "/":
    print(division(num1=a, num2=b))
else:
    print("Invalid operation")