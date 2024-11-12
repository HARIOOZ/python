from abc import ABC, abstractmethod
class car(ABC):
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    @abstractmethod
    def printdetails (self):
        pass
    
    def acceleration(self):
        print("speeds 100+kmph")
    def break_appllied(self):
        print("slow down to 20kmph")
class van(car):
    def printdetails(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("year:",self.year)
    def sunroof(self):
        print("athonnum illa")
class suv(car):
    def printdetails(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("year:",self.year)
    def refrigerator(self):
        print("athum illa")
van1=van("maruthi","omini",2004)
suv1=suv("tata","bolero",2005)
van1.acceleration()
suv1.refrigerator()
suv1.printdetails()
van1.accelerati()