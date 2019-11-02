from integer import Integer


def fun():
    num = input("Enter a number: ")
    for i in range(Integer(num) + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


fun()
