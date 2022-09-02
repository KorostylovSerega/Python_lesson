from datetime import date as dt
import calendar


class Employee:

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def __lt__(self, other) -> bool:
        return self.salary < other.salary

    def __le__(self, other) -> bool:
        return self.salary <= other.salary

    def __eq__(self, other) -> bool:
        return self.salary == other.salary

    def __ne__(self, other) -> bool:
        return self.salary != other.salary

    def __gt__(self, other) -> bool:
        return self.salary > other.salary

    def __ge__(self, other) -> bool:
        return self.salary >= other.salary


    def work(self) -> str:
        return 'I come to the office.'

    def check_salary(self, days: [int, list] = None) -> int:  # days = [d, m, yyyy] or days = int
        if isinstance(days, int):
            return self.salary*days

        elif isinstance(days, list):
            d, m, y = days

        elif days is None:
            y, m, d  = str(dt.today()).split('-')

        else:
            raise TypeError('check_salary() expects a data type int or list')

        weekdays = calendar.Calendar().itermonthdays2(int(y), int(m))
        days = sum([1 for day in weekdays if 0<day[0]<=int(d) and day[1] not in (5, 6)])  # including today
        return self.salary*days


class Recruiter(Employee):

    def __init__(self, name: str, salary: int):
        super().__init__(name, salary)

    def __str__(self) -> str:
        return f'{__class__.__name__}: {self.name}'


    def work(self) -> str:
        return 'I come to the office and start to hiring.'
   

class Developer(Employee):

    def __init__(self, name: str, salary: int, tech_stack: list = []):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def __str__(self) -> str:
        return f'{__class__.__name__}: {self.name}'

    def __add__(self, other) -> object:
        return Developer(name = f'{self.name} {other.name}',
                         salary = max(self.salary, other.salary),
                         tech_stack = list(set(self.tech_stack + other.tech_stack)))

    def __lt__(self, other) -> bool:
        if not self.tech_stack and not other.tech_stack:
            return super().__lt__(other)
        else:
            return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other) -> bool:
        if not self.tech_stack and not other.tech_stack:
            return super().__le__(other)
        else:
            return len(self.tech_stack) <= len(other.tech_stack)

    def __eq__(self, other) -> bool:
        if not self.tech_stack and not other.tech_stack:
            return super().__eq__(other)
        else:        
            return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other) -> bool:
        if not self.tech_stack and not other.tech_stack:
            return super().__ne__(other)
        else:        
            return len(self.tech_stack) != len(other.tech_stack)

    def __gt__(self, other) -> bool:
        if not self.tech_stack and not other.tech_stack:
            return super().__gt__(other)
        else:        
            return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other) -> bool:
        if not self.tech_stack and not other.tech_stack:
            return super().__ge__(other)
        else:        
            return len(self.tech_stack) >= len(other.tech_stack)


    def work(self) -> str:
        return 'I come to the office and start to coding.'



if __name__ == '__main__':

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

    print(emp1>emp2)
    print(rec1>rec2)
    print(dev1>dev2) # comparison by salary
    print(dev3>dev4) # comparison by tech_stack
    print(emp1<rec2)
    print(emp1<rec2<dev1) # comparison by salary
    print()
    
    print(rec2) # __str__
    print(dev3) # __str__
    print()

    print(emp1.check_salary(10)) # salary for 10 days
    print(rec2.check_salary([31, 8, 2022])) # salary for august
    print(rec1.check_salary(['31', '08', '2022'])) # salary for august
    print(dev2.check_salary()) # salary from the first day of the month until today
    print()

    print((dev3+dev4).__dict__) # new object
    print((dev1+dev2).__dict__) # new object
    print((dev1+dev2+dev3+dev4).__dict__) # new object
