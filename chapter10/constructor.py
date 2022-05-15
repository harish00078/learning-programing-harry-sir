# important point about constructor.
# 1.> it takes (self) arguments and can also takes further arguments.

# example for constructor.

class employee:
    company = "google"
    
    def __init__(self,name,salary,subunit): # (__init__) is a method that will run automatically.this is also know as constructor.
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("employee is created")
        
    def getdetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the name of the employee is {self.salary}")
        print(f"the name of the employee is {self.subunit}")
        
        
        
    def getsalary(self, signature):
            print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")
        # print("salary is 100k")
    
    # using static method we can create many function we want without using the arguments. 
    @staticmethod
    def greet():
        print("good morning , sir")
        
    @staticmethod
    def time():
        print("the time is 8pm in the evening")
        

harry = employee("harry",100,"youtube",)
harry.getdetails()
        
        
        

        


