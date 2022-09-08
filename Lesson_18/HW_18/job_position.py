"""
This module contains classes
Recruiter and Developer.
"""

from employee import Employee


class Recruiter(Employee):
    """
    This class inherits class Employee, and
    contains parameters of Recruiters.
    """

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

    def __init__(self, name: str, salary: int, email: str, tech_stack: list = None):
        """
        This constructor initializes the properties
        of objects of the class Developer.

        Input Arguments:
            name: str
                Developer name
            salary: int
                Working day salary
            email: str
                Developer email
            tech_stack: list(=None)
                List of technologies owned by the developer,
                empty list by default
        """
        super().__init__(name, salary, email)
        self.tech_stack = tech_stack
        if self.tech_stack is None:
            self.tech_stack = []

    def __str__(self) -> str:
        return f'{__class__.__name__}: {self.name}'

    def __add__(self, other) -> object:
        """
        This method will return a new instance
        of the developer class.
        """
        name = f'{self.name} {other.name}'
        salary = max(self.salary, other.salary)
        email = f'{self.email} {other.email}'
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        return Developer(name, salary, email, tech_stack)

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
