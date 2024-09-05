class Cup:
    def __init__(self,size,quantity):
        self.size=size
        self.quantity=quantity
    def cup_status(self):
        status = self.size - self.quantity 
        return status
    def cup_fill(self, fill):
        
        if self.quantity + fill <= self.size:
            self.quantity += fill  
        else:
            self.quantity = self.size  
        return self.quantity 

cup = Cup(100, 50)
print(cup.cup_status())
cup.cup_fill(40)
cup.cup_fill(20)
print(cup.cup_status())
