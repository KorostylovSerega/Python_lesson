# для работы программы файл 'fizz_buzz_data.txt' необходимо разместить в той же директории
name_data = 'fizz_buzz_data.txt'
file_data = open(name_data)
name_res = 'fizz_buzz_res.txt'
file_res = open(name_res, 'w')


for line in file_data:
    list = line.split()

    for i in range(1, int(list[2])+1):
        if i % int(list[0]) == 0 and i % int(list[1]) == 0:
            print('FB', end=' ')
            file_res.write('FB ')
        elif i % int(list[0]) == 0:
            print('F', end =' ')
            file_res.write('F ')
        elif i % int(list[1]) == 0:
            print('B', end =' ')
            file_res.write('B ')
        else:
            print(i, end =' ')
            file_res.write(str(i)+' ')

    print('\n')
    file_res.write('\n')

file_data.close()
file_res.close()
