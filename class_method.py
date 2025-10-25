from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Student:
    school: ClassVar[str]  # this  class variable
    name: str #thease are class object variables
    age: int

    def print_student_info(self):  #self tag eken refer krnne class eken hadhana object ekea meeka object eke method ekk
        print(f"name {self.name}")
