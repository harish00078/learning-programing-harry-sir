# object oriented programming:
# 1.> solving a problem by creating objects is one of the most popular approaches in programming.this is called object oriented programming.
# 2.> this concept focuses on using reusable code.


# write the code in this way is called = Procedural Programming
# a = 12
# b = 34

# print("the sum of the a and b is ", a+b)

# write code in object oriented programming.

class number:
    def sum(self):
        return self.a +self.b
    
    
num = number()
num.a = 12
num.b = 34
s = num.sum()
print(s) 

# class:
# 1> a class is a blueprint or template for creating objects.


# what is EmployeeName here in class.
# class EmployeeName:
'''
pascalcase:
EmployeeName --->pascalcase

camelcase:
isnumeric,isfloatorint --->camelcase'''


#object:
# 1> an object is an instantiation of  a class . when class is defined, the template is defined . memory is allocated only after object instantiation.