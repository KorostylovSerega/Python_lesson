l_bill = [1000, 500, 200, 100, 50, 10, 5]

wish_sum = int(input('Введите сумму: '))
print()

while wish_sum < 5:
    print('Минимальная сумма доступная для снятия 5 грн\n')
    wish_sum = int(input('Введите сумму: '))
    print()
else:
    r_sum = wish_sum

    for x in l_bill:
        if r_sum // x:
            q_bill = r_sum // x
            r_sum -= q_bill * x
            print('Выдано купр ' + str(q_bill) + 'шт по ' + str(x) + ' грн\n')
    if r_sum == 0:
        print('Выдано всю запрашиваемую сумму')
    else:
        print('Выдано ' + str(wish_sum - r_sum) + ' грн из ' + str(wish_sum) + ' грн запрошенных') 
