from tire.Tire import Tire


class CarriganTire(Tire):
    def __init__(self, arr):
        super().__init__(arr)

    def needs_service(self):
        for i in self.arr:
            if i >= 0.9:
                return True
        return False

