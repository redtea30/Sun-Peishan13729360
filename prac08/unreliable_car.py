from car import Car
from random import randint


class UnreliableCar(Car):


    def __init__(self, name, fuel, reliability):
        """call the Car's version of __init__, then set the reliability to the incoming value"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """generate a random number between 1 and 100"""
        random_number = randint(1, 100)
        # Only can drive if the number is less than the reliability of the car
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
