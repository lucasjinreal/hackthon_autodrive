"""

"""

from src.car import Car


if __name__ == '__main__':
    car = Car()

    try:
        car.set_speed(100, 100)

    except KeyboardInterrupt:
        car.__del__()

