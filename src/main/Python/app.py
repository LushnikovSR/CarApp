from pickup import Pickup
from conf import Fuels, GearBox


def main():
    my_car = Pickup("ford", "F-150", Fuels.DIS.value, GearBox.AUTO.value, "Dark Blue", 5000, 490)
    print(my_car.refill())


if __name__ == "__main__":
    main()
