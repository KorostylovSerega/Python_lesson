from statistics import mean


students = {
    'Мороз Артем': [8,8,9],
    'Стебенев Дмитрий':[8,9,10],
    'Степанов Максим':[10,9,3],
    'Лебеденко Роман':[4,3,5],
    'Фаркаш Ярослав':[6,10,10],
    'Семченко Дмитрий':[0,0,0],
    'Говоровский Дмитрий':[6,8,10],
    'Петриченко Александр':[0,0,0],
    'Коленов Марк':[3,9,2],
    'Соловинская Евгения':[6,0,0],
    'Шевцов Павел':[6,10,7],
    'Гаркуша Павел':[9,9,9],
    'Пономаренко Григорий':[7,0,0],
    'Параничев Александр':[7,10,9],
    'Хан Даниил':[3,8,8],
    'Крылов Руслан':[8,8,8],
    'Коростылев Сергей':[10,10,9],
    'Макаренко Владислав':[5,9,9],
    'Ригас Артур':[0,0,0]
    }

students_mean = {k: float('{0:.1f}'.format(mean(v))) for k, v in students.items()}

print("""'Рейтинг студентов по успеваемости' - введите '1'
'Студенты с худшей успеваемостью'   - введите '2'
'Студенты с лучшей успеваемостью'   - введите '3'""")
print()

answer = int(input('Введите значение:'))
print()

while answer not in (1,2,3):
    answer = int(input('ERROR\nПовторите ввод:'))
    print()

if answer == 1:
    rate = sorted(students_mean.items(), key = lambda item: item[1], reverse=True)
    list(map(lambda x: print(x[0],'==>',x[1]), rate))
elif answer == 2:
    min_grade = min(students_mean.values())
    low_student = list((k, v) for k, v in students_mean.items() if v == min_grade)
    list(map(lambda x: print(x[0],'==>',x[1]), low_student))
elif answer == 3:
    max_grade = max(students_mean.values())
    upp_student = list((k, v) for k, v in students_mean.items() if v == max_grade)
    list(map(lambda x: print(x[0],'==>',x[1]), upp_student))




