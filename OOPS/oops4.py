# Class Methods and Static Methods

class Employee:
    raise_p = 10/100
    number_of_employees = 0

    def __init__(self, name, series, company, pay):
        self.name = name
        self.series = series
        self.company = company
        self.pay = pay

        Employee.number_of_employees += 1

    def print_email_id(self):
        print(self.name + '@' + self.company + '.com')

    def get_raise(self):
        self.pay = self.pay + self.raise_p * self.pay

        return self.pay


obj1 = Employee('chella', 'The Ranch', 'Toyota', 50000)
obj2 = Employee('sai', 'dexter', 'norton', 130000)
