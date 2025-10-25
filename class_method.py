from dataclasses import dataclass
from typing import ClassVar

@dataclass

class_v = 10

class Student:
    school : ClassVar[str] # this also class veriable
    name : str
    age : int