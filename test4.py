class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)


class Teacher(Person):
    def __init__(self, name, age, subject):
        self.subject = subject

        Person.__init__(self, name, age)


myTeacher = Teacher("Dr. Hirani", 49, "Computer Science")
myTeacher.print_info()
print(myTeacher.subject)


intro = "My name is Jeff!"
print(intro.split()) # prints ['My', 'name', 'is', 'Jeff!']
print(intro.split('name')) # prints ['My ', ' is Jeff!']
print(intro.split('!')) # prints ['My name is Jeff', '']

my_tuple = (65, 2, 88, 101, 25)
max1 = max(my_tuple) # returns 101
print(max1)
