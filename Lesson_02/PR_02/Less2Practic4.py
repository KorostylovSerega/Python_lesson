#Ввести число, вывести его разряды и их множители
num = input('enter number: ')
num = list(reversed(num))
long_num = len(num)


for i in range(long_num):
    #print(int(num[i]) * 10 ** i)
    #print('разряд ' + str(i+1) + ' множитель ' + num[i])
    print(num[i] + '*10**' + str(i))



