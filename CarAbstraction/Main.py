from Motorcycle import Motorcycle
from Car import *
from Boat import *

from abc import ABC, abstractmethod

#Using Abstraction

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

car = Car()
motorcycle = Motorcycle()
boat = Boat()

car.go()
car.stop()

motorcycle.go()
motorcycle.stop()

boat.go()
boat.stop()