# для работы программы файл 'fizz_buzz_data.txt' необходимо разместить в той же директории
def fizzbuzz (f, b, n):

    fb_list = []

    for i in range(1, n+1):
        if not i % f and not i % b:
            fb_list.append('FB')
        elif not i % f:
            fb_list.append('F')
        elif not i % b:
            fb_list.append('B')
        else:
            fb_list.append(str(i))
    return ' '.join(fb_list)


file_data = open('fizz_buzz_data.txt')
file_res = open('fizz_buzz_res.txt', 'w')

for line in file_data:
    f, b, n = map(int, line.split())
    print(fizzbuzz(f, b, n))
    file_res.write(fizzbuzz(f, b, n) +'\n')
    
file_data.close()
file_res.close()
