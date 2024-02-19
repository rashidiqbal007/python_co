# Special (Magic/Dunder) Methods
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"

    
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return

    def __repr__(self):
        pass 

    def __str__(self):
        pass

    
    
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
