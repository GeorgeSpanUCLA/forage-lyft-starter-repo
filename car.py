from abc import ABC, abstractmethod
from engine.EB import Engine
from engine.EB import Battery
from Tires import Tires

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
        


class Car(Serviceable):
    def __init__(self, engine:Engine, battery:Battery, TireSet:Tires):
        self.engine  = engine
        self.battery = battery
        self.TireSet = TireSet
    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.TireSet.Tneeds_service()
       