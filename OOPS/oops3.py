# class variables

# class variables are variables that are shared by all the instances of the class
# instance variable is unique for each instance of the class
# class variable should be the same for all the instances
class Employee:
    # class variable
    raise_p = 10/100
    number_of_employees = 0

    def __init__(self, name, series, company, pay):
        # instance variable
        self.name = name
        self.series = series
        self.company = company
        self.pay = pay

        # here we use Employee instead of self bcz we do not need class variable to be overridden
        Employee.number_of_employees += 1

    def print_email_id(self):
        print(self.name + '@' + self.company + '.com')

    # how to use a class variable inside a method
    def get_raise(self):
        # way1 - wrong - syntax error - variable not defined error
        #self.pay = self.pay + raise_p*self.pay

        # way2 - right
        # In the below code only class variable is used
        #self.pay = self.pay + Employee.raise_p * self.pay

        # way3 - right
        # if raise_p is both instance attribute and class attribute then in the below code
        # instance attribute is used
        # class instance is overridden by instance variable
        self.pay = self.pay + self.raise_p * self.pay

        return self.pay


obj1 = Employee('chella', 'The Ranch', 'Toyota', 50000)
obj2 = Employee('sai', 'dexter', 'norton', 130000)

print(obj1.get_raise())

# check all the objects can access the class variable outside
# here obj1 is not accessing it's attribute, it tries to find the parent class's attribute
print(obj1.raise_p)
print(obj2.raise_p)

# try to change one of the object's class variable outside
obj2.raise_p = 20/100
# here class variable raise_p is not changing, but we are creating a new attribute to obj2 and assign it with a value

print(obj1.raise_p)
print(obj2.raise_p)
print(Employee.raise_p)
# above, we access class variable in obj1 and instance variable in obj2 which is newly created in line 43
print(obj2.get_raise())
# as you can see obj2 raise is calculated according to the 20% rate

# How to get to know about the attributes in a class and it's instances
# how to print out the namespace
print(obj1.__dict__)
print(Employee.__dict__)
print(obj2.__dict__)

# what if we wanna change the class attribute for all the instances
Employee.raise_p = 0.3
print(obj1.raise_p)
# here alone it shows 0.2 bcz we have created duplicate instance attribute raise_p in line 43 same as the class variable raise_p
print(obj2.raise_p)
print(Employee.raise_p)

# get total number of instances created
print(Employee.number_of_employees)
