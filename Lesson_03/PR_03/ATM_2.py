bill_list = [10, 20, 50, 100, 200, 500, 1000]
inp_sum = int(input('Введите сумму: '))
print()
cal_list = []

while inp_sum < 10 or inp_sum % 10 != 0:
    if inp_sum <10:
        print('Минимальная сумма доступная для снятия 10 грн\n')
        inp_sum = int(input('Введите сумму: '))
        print()
    else:
        print('Cумма недоступна для снятия\n')
        inp_sum = int(input('Введите сумму кратную 10 грн: '))
        print()
else:
    cal_sum = inp_sum
    for x in bill_list:
        i = 0    
        if x in (10, 50, 100, 500):
            while cal_sum >= x and i < 9:
                cal_sum -= x
                i += 1
            cal_list.append(i)
        elif x in (20, 200):
            while cal_sum >= x and i < 8:
                cal_sum -= x
                i += 1
            cal_list.append(i)
        else:
            while cal_sum >= x:
                cal_sum -= x
                i += 1
            cal_list.append(i)

    if cal_sum != 0:
        if cal_sum > 600:
            cal_list[5] = cal_list[5] + 1
            cal_sum -= 500
        
        if cal_sum > 400:
            cal_list[4] = cal_list[4] + 1
            cal_sum -= 200

        if cal_sum > 200:
            cal_list[3] = cal_list[3] + 1
            cal_sum -= 200

        if cal_sum > 100:
            cal_list[3] = cal_list[3] + 1
            cal_sum -= 100

        if cal_sum > 50:
            cal_list[2] = cal_list[2] + 1
            cal_sum -= 50

        if cal_sum > 30:
            cal_list[1] = cal_list[1] + 1
            cal_sum -= 20

        if cal_sum > 10:
            cal_list[1] = cal_list[1] + 1
            cal_sum -= 20

        if cal_sum == 10:
            cal_list[0] = cal_list[0] + 1
            cal_sum -= 10

        for i, x in enumerate(cal_list):
            if x != 0:
                print('Выдано ' + str(x) + ' купюр по ' + str(bill_list[i]) + ' грн')
        print('На общюю сумму ' + str(inp_sum) + ' грн ')
    else:
        for i, x in enumerate(cal_list):
            if x != 0:
                print('Выдано ' + str(x) + ' купюр по ' + str(bill_list[i]) + ' грн')
        print('На общюю сумму ' + str(inp_sum) + ' грн ')
    

     



        
