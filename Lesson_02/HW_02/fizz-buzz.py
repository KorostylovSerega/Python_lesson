fizz = int(input('enter number 1: '))
buzz = int(input('enter number 2: '))
jazz = int(input('enter number 3: '))

i=1


while i <= jazz:
    if i % fizz == 0 and i % buzz == 0:
        print('FB', end=' ')
        i += 1
    elif i % fizz == 0:
        print('F', end=' ')
        i += 1
    elif i % buzz == 0:
        print('B', end=' ')
        i += 1
    else:
        print(i, end=' ')
        i += 1

       
        
