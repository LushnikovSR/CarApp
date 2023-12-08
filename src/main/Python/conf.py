from enum import Enum


class Fuels(Enum):
    GAS = "gasoline"
    DIS = "diesel"
    CNG = "compressed natural gas"
    E85 = "biofuel ethanol"


class BodyType(Enum):
    COUPE = "Coupe"
    SEDAN = "Sedan"
    MPV = "Multi-Purpose Vehicle"
    HATCHBACK = "Hatchback"
    TRUCK = "Truck"
    MINIVAN = "Minivan"
    PICKUP = "Pickup"
    ESTATE = "Estate"


class NumberWheels(Enum):
    Four = 4


class GearBox(Enum):
    MT = "manual transmission"
    AUTO = "automatic transmission"
    CVT = "continuously variable transmission"
