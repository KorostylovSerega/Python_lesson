""" Homework lesson 19. With custom decorator """

import csv
import codecs
from functools import wraps
from urllib.request import urlopen


def generator_by_url(func):
    """
    This is a decorator for method generate_candidate,
     which creates class instances from csv files located at url.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        cls = args[0] if args else kwargs['cls']
        path = args[1] if args else kwargs['file_path']
        if path.startswith('http'):
            file = urlopen(path)
            reader = csv.reader(codecs.iterdecode(file, 'utf-8'))
            next(reader)
            objects = []
            for row in reader:
                objects.append(cls(row[0].split()[0], row[0].split()[1],
                                   row[1], row[2].split('|'), row[3], row[4]))
            return objects
        else:
            return func(*args, **kwargs)
    return wrapper


class Candidate:
    """
    This class contains parameters of
    candidates for the position.
    """

    def __init__(self, first_name: str, last_name: str, email: str,
                 tech_stack: list, main_skill: str, main_skill_grade: str):
        """
        This constructor initializes the properties
        of objects of the candidate class.

        Input Arguments:
            first_name: str
                Candidate name
            last_name: str
                Candidate surname
            email: str
                Candidate email
            tech_stack: list
                Technologies owned by the candidate
            main_skill: str
                Main specialization of the candidate
            main_skill_grade: str
                Candidates skill level
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self) -> str:
        """
        This method creates a new instance property, fullname.
        """
        return f'{self.first_name} {self.last_name}'

    @classmethod
    @generator_by_url
    def generate_candidate(cls, file_path: str) -> list:
        """
        This method creates new instances of the candidate class.

        Input Arguments:
            file_path: str
                Path to the *csv candidate data file

        Return:
            list: List of created objects
        """
        with open(file_path, newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            objects = []
            for row in reader:
                objects.append(cls(row[0].split()[0], row[0].split()[1],
                                   row[1], row[2].split('|'), row[3], row[4]))
            return objects
