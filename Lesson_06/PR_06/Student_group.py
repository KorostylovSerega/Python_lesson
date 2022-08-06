students = {
    'Мороз Артем': ['FrontEnd'],
    'Стебенев Дмитрий':['FrontEnd'],
    'Степанов Максим':['FullStack'],
    'Лебеденко Роман':['FrontEnd', 'Java'],
    'Фаркаш Яроcлав':['Java'],
    'Семченко Дмитрий':['Python', 'Java'],
    'Говоровский Дмитрий':['Python'],
    'Петриченко Александр':['Python'],
    'Коленов Марк':['FrontEnd'],
    'Соловинская Евгения':['Java'],
    'Шевцов Павел':['FullStack', 'FrontEnd'],
    'Гаркуша Павел':['Python', 'FrontEnd'],
    'Пономаренко Григорий':['FrontEnd'],
    'Параничев Александр':['Python', 'Java'],
    'Хан Даниил':['Python', 'FullStack'],
    'Крылов Руслан':['Python', 'FullStack'],
    'Коростылев Сергей':['Python', 'Java'],
    'Макаренко Владислав':['FrontEnd'],
    'Ригас Артур':['FullStack']
    }

print('Список студентов учащихся в двух и более группаx:\n')
#for key, item in sorted(students.items()):
#    if len(item)>1:
#        print(key)
list(map(print,(k for k, v in sorted(students.items()) if len(v)>1)))


print()
print('Список студентов не изучающих "FrontEnd":\n')
#for key, item in sorted(students.items()):
#    if not 'FrontEnd' in item:
#        print(key)
list(map(print,(k for k, v in sorted(students.items()) if not 'FrontEnd' in v)))


print()
print('Список студентов изучающих "Python" или "Java":\n')
#for key, item in sorted(students.items()):
#    if 'Java' in item or 'Python' in item:
#        print(key)
list(map(print,(k for k, v in sorted(students.items()) if 'Java' in v or 'Python' in v)))

# что равильней использовать для перебора в этом случае, for или map?
# правильно ли применять map к list Comprehation, или нужно делать переменную для списка, а следующей строкой map к переменной списка?

