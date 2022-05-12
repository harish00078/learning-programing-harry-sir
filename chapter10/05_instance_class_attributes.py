from fcntl import F_GETPATH
from os import get_handle_inheritable


class employee:
    company = "google"
    salary = 100
    
    
harry = employee()
rajni = employee()
# if we did not created the instance attributes.that program automatically work with class attibutes.
# harry.salary = 300
# rajni.salary = 400 
harry.salary = 45 # In oops attributes firstly detect the instance attributes if we did not have instance attributes then the program will automatically shifted to the class attributes.
print(harry.salary)
print(rajni.salary)
# (rajni.address) will through the error beacuse this is not present in the instance class 
# print(rajni.address) 

















