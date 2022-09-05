"""
This module contains the Employee class.
"""

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


