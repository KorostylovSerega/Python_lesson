temp = int(input('Введите показатель окружающей температуры,°C: '))
print('Температура ' + str(temp) + '°C')


if -100 <= temp < -91:
    print('Установлен новый температурный рекорд!')
elif -91 <= temp < -50:
    print('Возможно вы находитесь в Антарктиде')
elif -50 <= temp < -30:
    print('Сильный мороз')
elif -30 <= temp < -15:
    print('Морозно')
elif -15 <= temp < 0:
    print('Холодно')
elif 0 <= temp < 15:
    print('Прохладно')
elif 15 <= temp < 25:
    print('Тепло')
elif 25 <= temp < 30:
    print('Умерено жарко')
elif 30 <= temp < 40:
    print('Очень жарко')
elif 40 <= temp < 50:
    print('Возможно сейчас Июль и Вы в Ташкенте')
elif 50 <= temp < 57:
    print('Скорее всего Вы в "Долине Смерти" штат Калифорния')
elif 57 <= temp < 70:
    print('Установлен новый температурный рекорд!')
else:
    print('Введены некорректные показатели температуры\n'
          'Температура должна быть в диапазоне от -100°C до +70°C')
