# 1question: create a class programmer for storing information of few programmer working at microsoft

class programmer:
    company = "microsoft" 
    
    def __init__(self,name,product):
        self.name = name
        self.product = product
        
    def getinfo(self):
        print(f"the name of the company: {self.company} programmer is: {self.name} and the product is: {self.product}")
        
        
        
        
harry = programmer("harry","skype")
alka = programmer("alka","github")   
harry.getinfo()            
alka.getinfo()