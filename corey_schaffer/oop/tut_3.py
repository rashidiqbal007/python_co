# reguar, class & static methods
#https://youtu.be/rq8cL2XMM5M?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
# ------------------------------DESCRIPTION=====================================================
#regular methods in class auto take instance as first argumanet calling it self.
#class methods take cls as a first argument
# static methods take nth as first arg or can say dont use cls or self 
# _______________________________________________________________________________________

class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"

        Employee.num_of_emps += 1
    
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        # we want to use instace raise amount as it is diff from instance to instance thats why we used self.raise not Employee.rasie
        # we can use EMployee.raise if we wanted it to be same in all instances like no. of employee increase by +1 everytime we create new employee
        self.pay = int(self.pay * self.raise_amount)
        return
    
#CLASS METHOD-------------------================================-----=====-----------------------==================================
    # class method: used to set/change override class variable,methods(functionality) in all instances + can be used as alternative constructor in order to provide multiple ways to create objects
    @classmethod
    def raise_class_amount(cls,amount):
        cls.raise_amount  = amount

#STATIC METHOD---------------------------------------------------
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee("rashid","Iqbal",3200)
emp_2 = Employee("majid","iqbal",4500)


#static method being used that doesnt use any instance etc of its class
import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))










# print(Employee.num_of_emps)  #0

# emp7 = Employee("q", "t", 2300)
# print(Employee.raise_amount)
# print(emp7.pay)
# emp7.apply_raise()
# print(emp7.pay)
# # increases everytime instance is called
# print(Employee.num_of_emps) #1


# print(emp7.__dict__)
# # print(Employee.__dict__)

# Employee.raise_class_amount(1.07)

# print(Employee.raise_amount)
# print(emp7.raise_amount)








