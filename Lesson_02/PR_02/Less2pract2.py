#Прверить является ли число не четным, делиться ли на 3 и 5 одновременно,и не делиться на 10
num = int(input("enter number: "))
if num % 2 != 0 and num % 3 ==0 and num % 5 ==0 and num % 10 != 0:
    print(num)
else:
    print("number does not satisfi")

