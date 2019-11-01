from integer import Integer


def fun():
    num = input("Enter a number: ")
    for i in range(Integer(num)):
        print("*", end=' ')


fun()

