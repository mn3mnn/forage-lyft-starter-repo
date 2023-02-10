import unittest
from tire.CarriganTire import CarriganTire
from tire.OctoprimeTire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_should_be_service(self):
        tire = CarriganTire([0.1, 0, 1, 0.9])
        self.assertTrue(tire.needs_service())

    def test_should_not_be_serviced(self):
        tire = CarriganTire([0.5, 0.2, 0, 0.8])
        self.assertFalse(tire.needs_service())


class TestOctoptimeTire(unittest.TestCase):
    def test_should_be_service(self):
        tire = OctoprimeTire([0.5, 0.5, 1, 1])
        self.assertTrue(tire.needs_service())

    def test_should_not_be_serviced(self):
        tire = OctoprimeTire([0.1, 0.5, 1, 0.9])
        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()

