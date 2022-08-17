"""
Instance of a class
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f'name of dog is {self.name} and age is {self.age}')


d = Dog("shadow", 9)
d.details()


# Class Method

class Dog:
    name = 'Dog'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def info(cls):
        return cls.name


print(Dog.info())


# Static Method
"""
It is a method that can only be accessible by that class name.
"""
class Dog:
    name = 'student'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def info():
        return "This is a Dog class"


print(Dog.info())
