#Написать функцию которая будет простое число возводить в квардрат.

#Необходимо возвести в квадрат все простые числа в списке используя функцию map

def squre(x):
    return x*x


def prime(x):
    for i in range(2, x // 2 +1):
        if x % i == 0:
            return False
    return True


def check(x):
    if prime(x):
        return squre(x)
    else:
        return 0

print(list(map(check, range(2, 101))))


