# 2question: write a class  calculator capable of finding square,cube,and square root of a number.

class calculator:
    def __init__(self,num):
        self.number = num
    
    def square(self):
        print(f"the value of {self.number} square is {self.number**2}")
    
    def squareroot(self):
        print(f"the value of {self.number} square is {self.number**0.5}")
    
    def cube(self):
        print(f"the value of {self.number} square is {self.number**3}")
    
    
a = calculator(9)
a.square()
a.squareroot()
a.cube()