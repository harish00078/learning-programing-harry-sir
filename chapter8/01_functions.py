# functions: a function is a group of statements performing a specific task.
# when a program get bigger in size and its complexity grows ,it gets difficult for a programmer to keep track on which piece of the code is doing what!
# type of functions:
# 1. built in functions ->already persent in python(example of bulit in function is (len(),print(),range()etc)
# 2. user defined functions ->defined by the user.

def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] +marks[3])/400) *100
    return p
    
    # return ((marks[0] + marks[1] + marks[2] +marks[3])/400) *100
     


marks1 = [45,78,86,77] 
# percentage1 = (sum(marks)/400 ) * 100
# percentage1 = ((marks[0] + marks[1] + marks[2] +marks[3])/400) *100
percentage1 = percent(marks1)

marks2 = [75,98,88,78]
# percentage2 = (sum(marks2)/400) * 100
# percentage2 = ((marks[0] + marks[1] + marks[2] +marks[3])/400) *100
percentage2 = percent(marks2)


print(percentage1,percentage2)

# functions with arguments:
# 1. meaning  of arguments is gave some value to the function.
# 2. a function can accept the same values it can work with. we can put these values in the perenthises. a function can also return values as shown below in example.
def greet(name):
    gr = "hello" + name
    return gr


a = greet("harry")
# "harry" is passed to greet in name
# (a)  will now contain "hello harry"
    