from integer import Integer


def factor(x):
    f = 0

    for i in range(1, Integer(x)):
        if Integer(x) % i == 0:
            f = f + i

    print(f)


num = input("Enter a number: ")

factor(num)


