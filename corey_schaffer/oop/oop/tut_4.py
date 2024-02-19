#inheritance & creating subclasses of managers and developers


class Employee:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"


    def full_name(self):
        return '{} {}' .format(self.first,self.last)


class Tester(Employee):
    def __init__(self, first, last, pay, test_framework):
        super().__init__(first, last, pay)
        self.test_framework = test_framework



#inheritted all employee class functionality
class Developer(Employee):
    raise_amount = 1.7
    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first,last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)       

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->>', emp.full_name())

dev_1 = Developer("sa","as",34, "java")
dev_2 = Developer("majid", "iqbal", 3443, "python")

mgr_1 = Manager("sure", "as", 90000, [dev_1])
mgr_1.print_employees()

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_employees()

print(issubclass(Manager,Developer))



# emp_1 = Employee("sa","as",34)
# emp_2 = Employee("majid", "iqbal", 3443)
# emp_3 = Developer("sa","as",34,"Python")
# print(emp_3.prog_lang)


# print(help(Developer))

# print(emp_1.email)
# print(emp_3.email)








#NOTES
# Corey talks about inheritance of classes in this video.


# 1. What is inheritence?
# It is a method that allows us to create a new class that shares the same attributes and method with the original function, and add some extra functionality to the new class. It also does not disturb the original class.


# 2. How to make a class inherit from another class?
# class Developer(Employee):


# 3. Structure of classes and subclasses.
# When we input a function to a subclass, python follows the 'method resolution order', which is the chain of classes that it goes through to find what the method is. All classes have the built-in group of methods and attributes as their primary order.


# 4. How to initiate the subclass so that it can handle more information than its original class can?
# There are 2 ways.
# first, using the super method as follows and pass in the arguments in interest.
# super.__init__()


# Second, call the parent's init method explicitly and pass in the arguments in interest.
# Employee.init(self, first, last, )


# 5. Useful tools when exploring the inheritance system.
# .isinstance(instance, class)
# This method returns the boolean value of whether an instance belongs to a calss
# .issubclass(subclass, class)
# This method returns the boolean value of whether a class has inherited from the second class.


# 6. Example of class inheritance
# Whisky library 

# ++ when setting a default value for an ungiven argument, avoid using an empty mutable data type. That's a topic for another video.