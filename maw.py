class Employee:

    amountraise = 2000

    def __init__(self, first, last, pay, years):
        self.first = first
        self.last = last
        self.pay = pay
        self.years = years
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyyears(self):
        self.pay = int(self.pay + self.amountraise * self.years)

    # def total_amount(self):
    #     self.pay

emp1 = Employee('Maw', 'Besa', 20000, 2)
emp2 = Employee('Kei', 'Rimarim', 16000, 3)

print(emp1.pay)
emp1.applyyears()
print(emp1.pay)





# print(Employee.applyraise(emp1))
# print(Employee.fullname(emp2))
# print(emp1.email)
