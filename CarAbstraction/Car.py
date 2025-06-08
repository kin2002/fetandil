from abc import ABC, abstractmethod
from Vehicle import *

class Car(Vehicle):

    def go(self):
        print('You drive the car')

    def stop(self):
        print('You stop the car')
