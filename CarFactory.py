from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.Spindler import SpindlerBattery
from engine.Nubbin import NubbinBattery
from car import Car
from Tires import Carrigan, Octoprime, Tires
class CarFactory(object):
  
  def create_calliope(current_date:date, last_service_date:date, current_mileage:int , last_service_mileage:int): 
     Eng_A = CapuletEngine(current_mileage, last_service_mileage)
     Bat_A = SpindlerBattery(last_service_date,current_date)
     Tire = Carrigan()
     Car_C= Car(Eng_A, Bat_A,Tire)
     return Car_C


  def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
     Eng_A = WilloughbyEngine(current_mileage, last_service_mileage)
     Bat_A = SpindlerBattery(last_service_date,current_date)
     Tire = Octoprime()
     Car_G = Car(Eng_A, Bat_A,Tire)    
     return Car_G

  def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): 
     Eng_A = SternmanEngine(warning_light_on)
     Bat_A = SpindlerBattery(last_service_date,current_date)
     Tire = Octoprime()
     Car_G = Car(Eng_A, Bat_A,Tire)    
     return Car_G
     
  def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
     Eng_A = WilloughbyEngine(current_mileage, last_service_mileage)
     Bat_A = NubbinBattery(last_service_date,current_date)
     Tire = Octoprime()
     Car_G = Car(Eng_A, Bat_A,Tire)    
     return Car_G

  def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
     Eng_A = CapuletEngine(current_mileage, last_service_mileage)
     Bat_A = NubbinBattery(last_service_date,current_date)
     Tire = Octoprime()
     Car_G = Car(Eng_A, Bat_A,Tire)         
     return Car_G





