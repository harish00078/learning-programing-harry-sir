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

# check attributes --> firstly check is attributes persent in object? if we did not have attributes in object then program will automatically jump on the class attributes.
#                      secondly check is attributes persent in class?