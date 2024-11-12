from builtins import ValueError


def number():
    try:
        num=int(input("enter a number:"))
    except ValueError:
        print("error:enter a valid number")
    else:
        print(f"the enterd number is {num}")
number()
        
    