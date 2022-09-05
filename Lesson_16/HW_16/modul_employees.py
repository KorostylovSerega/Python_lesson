"""Lesson 16 Home Work."""


import calendar
from datetime import date as dt


class Employee:
    """
    This class contains parameters of employees.
    """

    def __init__(self, name: str, salary: int):
        """
        This constructor initializes the properties
        of objects of the employee class.

        Input Arguments:
            name: str
                Employee name
            salary: int
                Working day salary
        """
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
        """
        This method has no parameters
        and returns a string.
        """
        return 'I come to the office.'

    def check_salary(self, days: [int, list] = None) -> int:
        """
        This method calculates the salary
        based on the number of working days.

        Input Argument:
            days: int, list(=None)
                This parameter can take the number of days or
                the date until which the salary is calculated, by default
                the salary is calculated from the beginning of the month
                to the current date
                Example: days = int or days = [d, m, yyyy]: int, str

        Return:
            int: Amount of salary for days worked
        """

        def weekdays_amount(day=dt.today().day,
                            month=dt.today().month,
                            year=dt.today().year):
            """This function returns the amount of working days."""
            monthdays = calendar.Calendar().itermonthdays2(year, month)
            weekdays = 0
            for date in monthdays:
                if date[0] <= day:
                    if date[0] and date[1] not in (5, 6):
                        weekdays += 1
                    else:
                        continue
                else:
                    break
            return weekdays

        if isinstance(days, int):
            return self.salary * days
        elif isinstance(days, list):
            day, month, year = map(int, days)
            return weekdays_amount(day, month, year) * self.salary
        elif days is None:
            return weekdays_amount() * self.salary
        else:
            raise TypeError('check_salary expects a data type int or list')


class Recruiter(Employee):
    """
    This class inherits class Employee, and
    contains parameters of Recruiters.
    """

    def __init__(self, name: str, salary: int):
        """
        This constructor initializes the properties
        of objects of the class Recruiter.

        Input Arguments:
            name: str
                Recruiter name
            salary: int
                Working day salary
        """
        super().__init__(name, salary)

    def __str__(self) -> str:
        return f'{__class__.__name__}: {self.name}'

    def work(self) -> str:
        """
        This method has no parameters
        and returns a string.
        """
        return 'I come to the office and start to hiring.'
   

class Developer(Employee):
    """
    This class inherits class Employee, and
    contains parameters of developers.    
    """

    def __init__(self, name: str, salary: int, tech_stack: list = []):
        """
        This constructor initializes the properties
        of objects of the class Developer.

        Input Arguments:
            name: str
                Developer name
            salary: int
                Working day salary
            tech_stack: list(=[])
                List of technologies owned by the developer,
                empty list by default
        """
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def __str__(self) -> str:
        return f'{__class__.__name__}: {self.name}'

    def __add__(self, other) -> object:
        """
        This method will return a new instance
        of the developer class.
        """
        name = f'{self.name} {other.name}'
        salary = max(self.salary, other.salary)
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        return Developer(name, salary, tech_stack)

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
        """
        This method has no parameters
        and returns a string.
        """
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


