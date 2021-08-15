# Rather than initializing attributes manually we can initialize them when the class is instanciated
# we are gonna need a special init method to do it

class Employee:
    # we can consider init function as initializer
    # we can also consider it as constructor
    # when we define a function inside a class, then they recieve their instance as 1st argument automatically
    # by convention we call it self
    def __init__(self, name, series, company):
        self.name = name
        self.series = series
        self.company = company

    # like i said bfr functions inside a class has it's first argument = self
    # self is it's instance
    def print_email_id(self):
        print(self.name + '@' + self.company + '.com')


# we need to pass in all arguments when we instanciate the class
# it's like a normal function now where we need to pass all the necessary args for it to work
obj1 = Employee('chella', 'The Ranch', 'Toyota')
obj2 = Employee('sai', 'dexter', 'norton')

# way1: to call methods inside a class
obj1.print_email_id()
obj2.print_email_id()

# whenever we call a function inside a class using an object or instace,
# then that instace or object is automatically passed into the function as it's first argument
# we don't need to pass it explicitely

# Object == instance

# way2: to call methods inside a class
Employee.print_email_id(obj1)
Employee.print_email_id(obj2)
# as you can see in the above code we need to send the instance as first argument explicitely
