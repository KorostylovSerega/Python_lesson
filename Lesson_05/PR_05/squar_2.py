#Написать функцию которая будет простое число возводить в квардрат.

#Необходимо возвести в квадрат все простые числа в списке используя функцию map

def squar(num):

    for x in range(2, (num // 2 + 1)):
        if not num % x:
            return 0
        else:
            continue
    num = num ** 2
    return num

result = list(map(squar, range(2, 201)))
print(list(num for num in result if num))
