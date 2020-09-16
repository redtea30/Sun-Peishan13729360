from taxi import Taxi


class SilverServiceTaxi(Taxi):

    price_per_km = Taxi.price_per_km

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    flagfall = 4.5

    def __str__(self):
        """Return a string of a SilverServiceTaxi."""
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Refund of taxi fares."""
        # round fare result to nearest 10c
        fare = super().get_fare() + self.flagfall
        return fare

    def start_fare(self):
        """Start a new fare."""
        self.current_fare_distance = 0
