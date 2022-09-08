"""HW 18 test file"""

import traceback
from datetime import datetime

from employee import Employee, EmailAlreadyExistException
from job_position import Recruiter, Developer


def main():
    # creating class instances
    emp1 = Employee('Stepan', 150, 'stepan@gmail.com')
    emp2 = Employee('Anton', 120, 'Anton@gmail.com')
    rec1 = Recruiter('Julia', 200, 'Julia95@gmail.com')
    rec2 = Recruiter('Nasty', 180, 'Nastusya@gmail.com')
    rec3 = Recruiter('Nasty', 160, 'nastusya@gmail.com')
    dev1 = Developer('Taras', 220, 'taras@gmail.com')
    dev2 = Developer('Kirill', 250, 'Kirill89@gmail.com')
    dev3 = Developer('Max', 220, 'Maxus@gmail.com', ['python', 'c++', 'js', 'ruby'])
    dev4 = Developer('Andrey', 250, 'Andrey1997@gmail.com', ['python', 'c#', 'go'])

    print(emp1.work())
    print(rec2.work())
    print(dev3.work())
    print()

    # comparison by salary
    print(emp1 > emp2)
    print(rec1 > rec2)
    print(emp1 < rec2)
    print(emp1 < rec2 < dev1)
    print(dev1 > dev2)
    # comparison by tech_stack
    print(dev3 > dev4)
    print()

    # __str__
    print(rec2)
    print(dev3)
    print()

    # salary for 10 days
    print(emp1.check_salary(10))
    # salary for august
    print(rec2.check_salary([31, 8, 2022]))
    print(rec1.check_salary(['31', '08', '2022']))
    # salary from the first day of the month until today
    print(rec3.check_salary())
    print(dev2.check_salary())
    print()

    # new object
    print((dev3 + dev4).__dict__)
    print((dev1 + dev2).__dict__)
    print((dev1 + dev4).__dict__)

    # Calls an exception EmailAlreadyExistException
    print(dev2.validate())


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistException:
        with open('logs.txt', 'a+') as logs:
            logs.write(f'{datetime.today()} | {traceback.format_exc()}\n')
