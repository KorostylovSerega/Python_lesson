"""HW 17 test file"""

from employee import Employee
from job_position import Recruiter, Developer


if __name__ == '__main__':

    # creating class instances
    emp1 = Employee('Stepan', 150)
    emp2 = Employee('Anton', 120)
    rec1 = Recruiter('Julia', 200)
    rec2 = Recruiter('Nasya', 180)    
    dev1 = Developer('Taras', 220)
    dev2 = Developer('Kirill', 250)    
    dev3 = Developer('Max', 220, ['python', 'c++', 'js', 'ruby'])    
    dev4 = Developer('Andrey', 250, ['python', 'c#', 'go'])

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
    print(dev2.check_salary())
    print()

    # new object
    print((dev3 + dev4).__dict__)
    print((dev1 + dev2).__dict__)
    print((dev1 + dev2 + dev3 + dev4).__dict__)
