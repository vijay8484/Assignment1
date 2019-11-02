import math

from integer import Integer


def fun():
    num = input("Enter a number: ")
    digits = int(math.log10(Integer(num)))+1
    print(digits)


fun()
