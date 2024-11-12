from builtins import Exception


class NegativeNumberError(Exception):
    pass
def Check_positive(number):
    if number<0:
        raise NegativeNumberError("error:numbers are not allowed")
    print(f"number enterd:{num}")
try:
    num=int(input("enter a number:"))
    Check_positive(num)
except NegativeNumberError as e:
    print(e)    