from car import Car
from i_car_wash import ICarWash
from i_fuel_station import IFuelStation
from conf import BodyType, NumberWheels


class Pickup(Car, ICarWash, IFuelStation):
    load_capacity: int

    def __init__(self, make, model, fuel_type, gear_box_type, body_color, engine_cap, load_capacity):
        super().__init__(make, model, BodyType.PICKUP.value, NumberWheels.Four.value, fuel_type, gear_box_type,
                         body_color, engine_cap)
        self.load_capacity = load_capacity

    def refill(self):
        return "Car is fueled"

    def wip_headlights(self):
        return "Headlights is clear"

    def wip_mirrors(self):
        return "Mirrors is clear"

    def wip_windshield(self):
        return "Windshield is clear"
