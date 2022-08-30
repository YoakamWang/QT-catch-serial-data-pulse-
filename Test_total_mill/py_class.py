# import os
#
# cur_path = os.path.dirname(__file__)
# ab_path = os.path.abspath(__file__)
# print(ab_path)
# real_path = os.path.realpath(__file__)
# print(real_path)
# def site():
#     print("PythonGeeks")
# website = site
# print(f"{site = }")
# print(f"{website = }")
# site()
# website()
# def sqrt(num):
#     return num**3
# def square(num):
#     return num**2
# def math(function):
#     print(function(4))
# math(sqrt)
# math(square)
# def str1():
#     print("PythonGeeks")
# def func1():
#     return str1
# var1 = func1()
# var1()
# def math(num):
#     def square():
#         return num**2
#     print(square())
# math(2)
# def my_decor(func):
#     def my_wrap():
#         print("Decorator Function")
#         return func()
#
#     return my_wrap
#
#
# def my_function():
#     print("Main Function")
#
#
# my_function = my_decor(my_function)
# my_function()
# def my_decor(func):
#     def my_wrap(*args, **kwargs):
#         print("Decorator Function")
#         return func(*args, **kwargs)
#     return my_wrap
# @my_decor
# def my_function(str1, str2):
#     print("Main Function")
#     print(str1 + " are " +  str2)
# my_function("Mangoes", "Delicious")

# def my_decor(func):
#     def my_wrap(*args, **kwargs):
#         print("Decorator Function 1")
#         return func(*args, **kwargs)
#     return my_wrap
# def my_another_decor(func):
#     def my_wrap(*args, **kwargs):
#         print("Decorator Function 2")
#         return func(*args, **kwargs)
#     return my_wrap
# @my_decor
# @my_another_decor
# def my_function(str1, str2):
#     print("Main Function")
#     print(str1 + " are    " +  str2)
# my_function("Mangoes", "Delicious")
# Create a class say Employee
# class Employee:
#     # Inside the class, take a variable and initialize it with some random number.
#     salary = 3000
#
#     # Create a function/method say Getsalary() which accepts the class
#     # object as an argument
#     @classmethod
#     def Getsalary(cls_obj):
#         # Print the class variables by using the class object.
#         print("The salary of an Employee = ", cls_obj.salary)
#
#
# # Pass the Getsalary() method to the classmethod() function and store it as the
# # same function(Employee.Getsalary).
# # Employee.Getsalary = classmethod(Employee.Getsalary)
# # Call the above function.
# Employee.Getsalary()

# class Maths():
#
#     @staticmethod
#     def addNum(num1, num2):
#         return num1 + num2
#
#
# # Driver's code
# if __name__ == "__main__":
#     # Calling method of class
#     # without creating instance
#     res = Maths.addNum(10, 2)
#     print("The result is", res)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#         # a static method to check if a Person is adult or not.
#
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
#
# # Driver's code
# if __name__ == "__main__":
#     res = Person.isAdult(12)
#     print('Is person adult:', res)
#
#     res = Person.isAdult(22)
#     print('\nIs person adult:', res)

# print("Program to demonstrate the @property decorator is as follows:")
# print("\n")


# class Animals:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         print('Fetching the name')
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         print('Setting the name to ' + name)
#         self._name = name
#
#     @name.deleter
#     def name(self):
#         print('Deleting the set name')
#         del self._name
#
#
# a = Animals('Tiger')
# print(a.name)
# a.name = 'Lion'
# del a.name


class Person():
    salary = 30000

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    @staticmethod
    def addNum(num1, num2):
        return num1 + num2

    @classmethod
    # Create a function/method say Getsalary() which accepts the class
    # object as an argument
    def Getsalary(cls_obj):
        # Print the class variables by using the class object.
        print("The salary of an Employee = ", cls_obj.salary)

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


# Init a Person
person = Person('selva', 'prabhakaran')
print(person.fullname)  # > selva prabhakaran
print(person.first)  # > selva
print(person.last)  # > prabhakaran

# Setting fullname calls the setter method and updates person.first and person.last
person.fullname = 'velu pillai'

# Print the changed values of `first` and `last`
print(person.fullname)  # > velu pillai
print(person.first)  # > pillai
print(person.last)  # > pillai
del person.fullname

# Print the changed values of `first` and `last`
print(person.first)  # > None
print(person.last)  # > None
print(person.addNum(2, 3))
person.Getsalary()
