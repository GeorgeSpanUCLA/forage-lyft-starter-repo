from abc import ABC, abstractmethod
from array import array




class Tires(ABC):
    def __init__(self):
     self.TireArr = array('i',[0,0,0,0])
    
    def AddTyreWear(self,Tire, Wear):
     self.TireArr[Tire] = Wear


     @abstractmethod
     def Tneeds_service(self):
       pass


class Carrigan(Tires):
   def __init__(self):
    super().__init__()  
    self.maxWear = 0.9
    
    def Tneeds_service(self):
      for element in self.TyreArr:
          if element>=self.maxWear:
           return True
      return False


class Octoprime(Tires):
   def __init__(self):
    super().__init__()  
    self.maxWear = 3
    
    def Tneeds_service(self):
      sum = 0
      for element in self.TyreArr:
          sum = sum+element 
          if sum >=self.maxWear:
           return True
      return False



