from tire.Tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, arr):
        super().__init__(arr)

    def needs_service(self):
        return sum(self.arr) >= 3


