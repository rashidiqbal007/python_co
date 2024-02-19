# https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2
#  instance and class variables 
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"

        #emp num increases with num of objects/instantiation
        Employee.num_of_emps += 1
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        # we want to use instace raise amout as it is diff from instace to instance thats why we used self.raise not Employee.rasie
        # we can use EMployee.raise if we wanted it to be same in all instances like no. of employee increase by +1 everytime we create new employee
        self.pay = int(self.pay * self.raise_amount)
        return




print(Employee.num_of_emps)  #0

emp7 = Employee("q", "t", 2300)
print(Employee.raise_amount)
print(emp7.pay)
emp7.apply_raise()
print(emp7.pay)
# increases everytime instance is called
print(Employee.num_of_emps) #1


print(emp7.__dict__)
# print(Employee.__dict__)


# Employee.raise_amount = 1.05 #chnages globally the amount from 1.04 => 1.05
emp7.raise_amount = 1.05 #changes raise amount from 1.04 => 1.05 only in specific instance
print(Employee.raise_amount)
print(emp7.raise_amount)







