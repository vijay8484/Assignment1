from integer import Integer


def fun():
    num = input("Enter a number: ")
    for i in range(Integer(num)):
        for j in range(1, Integer(num)+1):
            print(j, end=' ')
        print()


fun()
