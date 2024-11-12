from builtins import ValueError, ZeroDivisionError


def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("error:pls typ a valid number")
    else:
        print(f"result after division{result}")
    
divide_numbers()




                
