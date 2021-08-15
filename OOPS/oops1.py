# https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

# A function associated with a class is called method
# A variable associated with a class is called attribute

# Define a class
class Employee:
    pass


# create instance of a class
obj1 = Employee()
obj2 = Employee()
# the above instances are unique and do not affect each other in any way

# Manually Create Attributes of a class
obj1.name = 'chella'
obj1.series = 'The Ranch'
obj1.company = 'toyota'

obj2.name = 'sai'
obj2.series = 'dexter'

print(obj1.company)
# print(obj2.company) --> this will provide us the error as company hasn't been initialized to obj2
