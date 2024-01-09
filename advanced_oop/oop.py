
class Person:

    __age = 25
    _working_hours = ['09:00 - 18:00']

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} | Age: {self.__age}'
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value
    

class Employee(Person):

    _working_hours = ['10:00 - 18:00']

    def __init__(self, first_name, last_name, department):
        super().__init__(first_name, last_name)
        self.department = department

    def __str__(self):
        return f'{self.first_name} {self.last_name} | Age: {self.age} | Department: {self.department}'
    


class Calc1:

    def __str__(self) -> str:
        return 'Calc1'
    

class Calc2:

    def __str__(self) -> str:
        return 'Calc2'
    

class Calc3(Calc1, Calc2):

    def __str__(self) -> str:
        return super(Calc1, self).__str__()
    

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def call(self):
        pass

    def display(self):
        return 'display'


class Car(Vehicle):

    def call(self):
        return 'This is a car!'
    

class Motorcycle(Vehicle):

    def call(self):
        return 'This is a motorcycle'
    
    def display(self):
        return 'test'
    
c = Car()
m = Motorcycle()

print(c.call())
print(m.call())