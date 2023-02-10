import unittest
from datetime import datetime

from engine.CapuletEngine import CapuletEngine
from engine.WilloughbyEngine import WilloughbyEngine
from engine.SternmanEngine import SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = CapuletEngine(30001, 0)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = CapuletEngine(20000, 100)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = SternmanEngine(datetime.today().date(), True)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = SternmanEngine(datetime.today().date(), False)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = WilloughbyEngine(60001, 0)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = WilloughbyEngine(60000, 0)
        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
    unittest.main()

