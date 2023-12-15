# dunder methods
# classmethods
# staticmethod

from datetime import datetime

class Person:

    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def get_fullname(self):
        return f'{self.name} {self.surname}'  
    
    @classmethod
    def get_fullname_from_str(cls, fullname, age):
        name, surname = fullname.split('-')
        return cls(name, surname, age)
    
    @classmethod
    def get_age_from_bday(cls, name, surname, bday):
        age = datetime.now().year - bday
        return cls(name, surname, age)
    
    @staticmethod
    def display():
        return 'Hello'


    def __repr__(self) -> str:
        return self.name

x = input()
# age = int(input())



p2 = Person.get_fullname_from_str('John-Doe', 20)

p3 = Person.get_age_from_bday('John', 'Doe', 2000)

print(p3.age)
# print(p2.surname)

    
# 'John', 'Doe', 2000
# 'John-Doe', 20
# p1 = Person('John', 'Doe', 20)

# print(p1.name)
# print(p1.age)
# print(p1.get_fullname())