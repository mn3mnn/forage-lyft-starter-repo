from Car import Car
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from engine.CapuletEngine import CapuletEngine
from engine.WilloughbyEngine import WilloughbyEngine
from engine.SternmanEngine import SternmanEngine
from tire.CarriganTire import CarriganTire
from tire.OctoprimeTire import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire([0, 0.5, 0, 0.8])
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTire([0, 0.5, 0, 0.9])
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire([0, 0.5, 1, 0.9])
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire([1, 0.6, 1, 0.9])
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = CarriganTire([0.2, 0.5, 0, 0])
        car = Car(engine, battery, tire)
        return car
