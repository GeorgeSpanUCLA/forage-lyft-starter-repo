from abc import ABC, abstractmethod
from engine.EB import Engine
from engine.EB import Battery

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
        


class Car(Serviceable):
    def __init__(self, engine:Engine, battery:Battery):
        self.engine  = engine
        self.battery = battery

    
    def needs_service(self):
        if self.engine.needs_service():
         return True
        if self.battery.needs_service():
           return True 
        else:
           return False
       
       