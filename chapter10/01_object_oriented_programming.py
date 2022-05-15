# object oriented programming:
# 1.> solving a problem by creating objects is one of the most popular approaches in programming.this is called object oriented programming.
# 2.> this concept focuses on using reusable code.
# defination of object oriented programming.
# In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data. 


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
# 2> objects of a given class can invoke the methods available to it without revaling the implementation details to the user.
# abstraction and encapsulation.


# modelling a problem in oops.
# we identify the following in our problem 
# noun ->class ->employee
# adjective -> attributes -> name,age,salary
# verbs -> methods -> getsalary(),increment().


#types of attributes:
#1.> class attributes.
#2.> instance attributes.

#1.> class attributes:
# an attribute that belongs to the class rather than a particular objects.
# example of class attributes:
# class employee:
    # company = "google"  --> [specific to each class]
    
    # harry = employee()  --> object instantiation
    # harry.company
    # employee.company = "youtube"  --> changing class attributes
    
    
#2.> instance(object) attributes:
# an attributes that belong to the instance(object)assuming the class from the previous example:
# example of the instance attributes:
#class employee:
   # company
   
   
   
# 'self' parameter :

# 1.> self refers to the instance of the class
# 2.> it is automiatically passed with a function call from an object.

# static method:
# 1.> sometimes we need a function that does not use the self parameter. 


# constructor:
#  1.> __init__() constructor;
#  __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also know as constructor.
# it takes self argument and can also take further arguments.

