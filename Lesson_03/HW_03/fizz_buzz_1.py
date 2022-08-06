# для работы программы файл 'fizz_buzz_data.txt' необходимо разместить в той же директории
name = 'fizz_buzz_data.txt'
file = open(name)


for line in file:
    list = line.split()

    for i in range(1, int(list[2])+1):
        if i % int(list[0]) == 0 and i % int(list[1]) == 0:
            print('FB', end=' ')
        elif i % int(list[0]) == 0:
            print('F', end =' ')
        elif i % int(list[1]) == 0:
            print('B', end ='')
        else:
            print(i, end =' ')
    print('\n')

file.close()
