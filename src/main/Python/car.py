from abc import ABC
from conf import *


class Car(ABC):
    make: str
    model: str
    body_type: str
    number_wheels: int
    fuel_type: str
    gear_box_type: str
    body_color: str
    engine_cap: int

    def __init__(self, make, model, body_type, number_wheels, fuel_type, gear_box_type, body_color, engine_cap):
        self.male = make
        self.model = model
        self.body_type = body_type
        self.number_wheels = number_wheels
        self.fuel_type = fuel_type
        self.gear_box_type = gear_box_type
        self.body_color = body_color
        self.engine_cap = engine_cap

    def movement(self):
        pass

    def maintenance(self):
        pass

    def trn_lights(self):
        pass

    def trn_wipers(self):
        pass
