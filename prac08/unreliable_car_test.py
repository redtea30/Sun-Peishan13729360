"""
Test Unreliable cars.
"""
from unreliable_car import UnreliableCar


def main():
    """Test unreliable car program"""
    car1= UnreliableCar("Car1", 100, 99)
    car2 = UnreliableCar("Car2", 100, 40)

    for km in range(1, 20):
        print("Attempting to drive {}km:".format(km))
        print("{:5} drove {:2}km".format(car1.name, car1.drive(km)))
        print("{:5} drove {:2}km".format(car2.name, car2.drive(km)))

    print(car1)
    print(car2)



main()
