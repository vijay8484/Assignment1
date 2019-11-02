from integer import Integer


def fact(x):

    f = 1

    for i in range(1, Integer(x) + 1):
        f = f * i
    return f


num = input("Enter a number: ")

result = fact(num)

print(result)
