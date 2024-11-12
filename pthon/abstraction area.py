from abc import ABC, abstractmethod
class area(ABC):
    @abstractmethod
    def area(self):
       pass                                        
class circlearea(area):
   def __init__(self,radius):
        self.radius=radius
   def area(self):
        print (f"area:{3.14*self.radius*2}")
class reactangle_area(area):
   def __init__(self,leng,bredth):
        self.leng=leng
        self.bredth=bredth
   def area(self):
       print  (f"area:{self.bredth*self.leng}")
reactangle_area1=reactangle_area(5,4)
circlearea1=circlearea(5)

reactangle_area1.area()
circlearea1.area()

    
        
    
        