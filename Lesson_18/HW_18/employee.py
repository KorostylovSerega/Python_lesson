"""
This module contains the Employee class and
class EmailAlreadyExistException.
"""

import traceback
import calendar
from datetime import datetime, date as dt


class EmailAlreadyExistException(Exception):
    """
    This class calls an exception EmailAlreadyExistException.
    """
    pass


class Employee:
    """
    This class contains parameters of employees.
    """

    def __init__(self, name: str, salary: int, email: str):
        """
        This constructor initializes the properties
        of objects of the employee class.

        Input Arguments:
            name: str
                Employee name
            salary: int
                Working day salary
            email: str
                Employee email
        """
        self.name = name
        self.salary = salary
        self.email = email
        self.save_email()

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

        def weekdays_amount(day_: int = dt.today().day,
                            month_: int = dt.today().month,
                            year_: int = dt.today().year):
            """This function returns the amount of working days."""
            monthdays = calendar.Calendar().itermonthdays2(year_, month_)
            weekdays = 0
            for date in monthdays:
                if date[0] <= day_:
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

    def validate(self):
        """
        This method checks that such an email address exists in the file.
        """
        try:
            with open('emails.txt') as file:
                if self.email.lower() in file.read():
                    raise EmailAlreadyExistException("This email is already recorded")
        except FileNotFoundError:
            with open('emails.txt', 'w'):
                pass

    def save_email(self):
        """
        This method writes the object's email address to a file
        if it hasn't been written before.
        """
        try:
            self.validate()
        except EmailAlreadyExistException:
            with open('logs.txt', 'a+') as logs:
                logs.write(f'{datetime.today()} | {traceback.format_exc()}\n')
        else:
            with open('emails.txt', 'a+') as file:
                file.write(self.email.lower() + '\n')
