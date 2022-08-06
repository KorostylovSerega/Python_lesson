def atm_calculation(amount):

    bill_list = [10, 20, 50, 100, 200, 500, 1000]
    reserve_amount = 0
    count_list = []

    for bill in bill_list:
        if amount >= bill:
            if bill in (10, 50, 100, 500):
                q_bill = amount // bill
                if q_bill > 9:
                    q_bill = 9
                    amount -= q_bill * bill
                    reserve_amount += bill
                    count_list.append(q_bill)
                else:
                    amount -= (q_bill - 1) * bill
                    if amount > reserve_amount:
                        amount -= bill
                        count_list.append(q_bill)
                    else:
                        count_list.append(q_bill - 1)
            elif bill in (20, 200):
                q_bill = amount // bill
                if q_bill > 8:
                    q_bill = 8
                    amount -= q_bill * bill
                    reserve_amount += bill * 2
                    count_list.append(q_bill)
                else:
                    amount -= (q_bill -1) * bill
                    if amount > reserve_amount:
                        amount -= bill
                        count_list.append(q_bill)
                    else:
                        count_list.append(q_bill - 1)                
            else:
                q_bill = amount // bill
                amount -= (q_bill -1) * bill
                if amount > reserve_amount:
                    amount -= bill
                    count_list.append(q_bill)
                else:
                    count_list.append(q_bill - 1)
        elif not amount:
            return list(zip(count_list, bill_list))
        else:
           count_list.append(0)

    reserve_amount = 1100

    bill_list.reverse()
    count_list.reverse()

    for i, bill in enumerate(bill_list[1:], 1):
        if amount >= bill:
            if bill in (200, 20):
                if amount > reserve_amount - bill:        
                    count_list[i] = count_list[i] + 2
                    amount -= bill*2
                elif amount > reserve_amount - bill*2:
                    count_list[i] = count_list[i] + 1
                    amount -= bill
                reserve_amount -= bill*2
            else:
                if amount > reserve_amount - bill:
                    count_list[i] = count_list[i] + 1
                    amount -= bill
                reserve_amount -= bill
        else:
            if bill in (200, 20):
                reserve_amount -= bill*2 
            else:
                reserve_amount -= bill
    
    bill_list.reverse()
    count_list.reverse()

    return list(zip(count_list, bill_list))


amount = int(input('Введите сумму: '))
print()

while amount < 10 or amount % 10:
    if amount < 10:
        print('Минимальная сумма доступная для снятия 10 грн\n')
        amount = int(input('Введите сумму больше 10 грн: '))
        print()
    else:
        print('Cумма недоступна для снятия\n')
        amount = int(input('Введите сумму кратную 10 грн: '))
        print()

final_count = atm_calculation(amount)
final_amount = sum(map(lambda value: value[0] * value[1], final_count))
#final_amount = sum(value[0] * value[1] for value in final_count)
#каким способом правильнее подсчитать final_amount?

print('Выдано купюр: ', end='')
for value in final_count:
    qty, nominal = map(int, value)
    if qty:
        print('{:2} шт по {} грн'.format(qty, nominal))
        print(' '*len('Выдано купюр: '), end='')
print()
print('На общюю сумму: {} грн'.format(final_amount))
