class compdetails:
    
    def __init__(self,cpu,ram):
        self.cpu =cpu
        self.ram =ram
       
    def config(self):
        print("Config Is ",self.cpu,self.ram)
comp1=compdetails("i5","8")
comp2=compdetails("i7","9")

comp1.config()
comp2.config()


