#Ввести число и вывести все его делители
number = int(input("enter number: "))
for i in range(1, number+1):
    if not number % i:
        print(i)
