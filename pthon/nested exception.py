from builtins import ValueError, ZeroDivisionError


try:
    h=open(r'C:/Users/hari prasad e/Documents/softronics/assingme/hari.txt')
    try:
        content=h.read()
        print(content)
        num1=int(input("enter a number"))
        num2=int(input("enter a number"))
        result=num1%num2
        print(f"resul:{num1}%{num2}is{result}")
    except ZeroDivisionError:
        print("error:cannot divide by zero")
except FileNotFoundError as e:
    print(f"error:{e}")
except ValueError:
    print(f"error:invalid number")




    