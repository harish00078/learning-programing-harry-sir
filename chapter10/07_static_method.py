class employee:
    company = "Google"
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
        
        
        


harry = employee()
harry.salary = 100000
harry.getsalary("thanks!")
# harry.greet()
employee.greet()
harry.time()







