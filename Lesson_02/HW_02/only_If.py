import random

num = random.randint(1, 20)

print('Угадайте число от 1 до 20\n\n'
      'У Вас есть три попытки\n')

num_inp = int(input('Попытка №1: '))
i = 1


while i <= 3:
    if num_inp == num:
        print('\n'
              'Вы угадали с попытки №' + str(i))
        break

    if num_inp > 20 or num_inp < 1:
        print('\n'
              'Некорректный ввод, введите число от 1 до 20')
        num_inp = int(input('Повторите попытку: '))

    if num_inp >= 1 and num_inp <= 20 and num_inp > num and i < 3:
        print('\n'
              'Не угадали, попробуйте число меньше ' + str(num_inp))
        i += 1
        num_inp = int(input('Попытка №' + str(i) + ': '))

    if num_inp >= 1 and num_inp <= 20 and num_inp < num and i < 3:
        print('\n'
              'Не угадали, попробуйте число больше ' + str(num_inp))
        i += 1
        num_inp = int(input('Попытка №' + str(i) + ': '))

    if i == 3 and num_inp != num:
        print('\n'
              'Вы не угадали!\n'
              'Попыток больше нет')
        i += 1
