from integer import Integer


def fun():
    num = input("Enter a number: ")
    for i in range(Integer(num)):
        for j in range(Integer(num)-i):
            print("* ", end=' ')
        print()


fun()
