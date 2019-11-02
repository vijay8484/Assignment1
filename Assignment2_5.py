from integer import Integer


def prime(x):

    for i in range(2, Integer(num)):
        if Integer(num) % i == 0:
            print("Number is Not Prime")
            break
    else:
        print("Number is Prime Number")


num = input("Enter a number: ")

prime(num)


