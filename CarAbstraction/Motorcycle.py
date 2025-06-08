from Vehicle import *
from abc import ABC, abstractmethod

class Motorcycle(Vehicle):


    def go(self):
        print('You drive the Motorcycle')

    def stop(self):
        print('You stop the Motorcycle')
