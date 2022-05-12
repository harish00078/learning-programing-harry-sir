# class attributes example.

# class employee:
#     company = "google"
    
# harry = employee()
# rajni = employee()
# print(harry.company)
# print(rajni.company)
# employee.company = "youtube" # we can change the attribute in class attributes during the program
# print(harry.company)
# print(rajni.company)


# instance attribute example.
from cgitb import html


class employee:
    company = "google"
    
harry = employee()
rajni = employee()
harry.salary = 300
rajni.salary = 400  # these are the instance attributes.
print(harry.salary)
print(rajni.salary)

# note for the instance attributes :
# instance attributes takes prefrence over class attributes during assignment and retreival.

# harry attributes --> (1) is attributes1 persent in object?
#                      (2) is attributes1 persent in class?