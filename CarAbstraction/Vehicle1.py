from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass