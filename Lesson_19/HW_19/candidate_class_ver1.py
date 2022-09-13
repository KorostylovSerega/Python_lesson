""" Homework lesson 19"""

import csv
import codecs
from urllib.request import urlopen


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
    def generate_candidate(cls, file_path) -> list:
        """
        This method creates new instances of the candidate class.

        Input Arguments:
            file_path: str
                Path to the *csv candidate data file in directory,
                 or url

        Return:
            list: List of created objects
        """
        if 'http' in file_path:
            file = urlopen(file_path)
            reader = csv.reader(codecs.iterdecode(file, 'utf-8'))
            next(reader)
            objects = []
            for row in reader:
                objects.append(cls(row[0].split()[0], row[0].split()[1],
                                   row[1], row[2].split('|'), row[3], row[4]))
            return objects
        else:
            with open(file_path, newline='') as file:
                reader = csv.reader(file, delimiter=',')
                next(reader)
                objects = []
                for row in reader:
                    objects.append(cls(row[0].split()[0], row[0].split()[1],
                                       row[1], row[2].split('|'), row[3], row[4]))
                return objects
