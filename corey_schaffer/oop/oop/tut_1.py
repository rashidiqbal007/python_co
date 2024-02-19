# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def full_name(self):
        return '{} {}'.format(self.first, self.last)




emp7 = Employee()
print(emp7.full_name())









em = Employee("s", "s")
print(em.full_name())
# print(Employee.full_name(em))


emp_1 = Employee("rashid", "iqbal")


employee_new = Employee("sana","ali")
print(employee_new.full_name())


print(Employee.full_name(emp_1))
# emp_1.first_name = "Rashid" 
# emp_1.last = "Iqbal"


# emp_4.email = "rashid.iqbal@vyro.ai"

# print(emp5.first , emp_4.last)