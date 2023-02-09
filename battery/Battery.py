from abc import ABC, abstractmethod
import Serviceable


class Battery(ABC, Serviceable):
    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def needs_service(self):
        pass
