from abc import ABC, abstractmethod
from array import *


class Tire(ABC):
    arr = array('d', [])

    def __init__(self, arr):
        self.arr = arr

    @abstractmethod
    def needs_service(self):
        pass

