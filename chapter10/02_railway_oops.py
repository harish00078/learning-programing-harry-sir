class RailwayForm:
    formtype = "railwayform"
    def printdata(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")
        
    
harrysapplication = RailwayForm()
harrysapplication.name = "harry"
harrysapplication.train = "rajdhani express"
harrysapplication.printdata()



     