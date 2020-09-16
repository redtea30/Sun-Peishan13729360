from silver_service_taxi import SilverServiceTaxi


def main():

    my_taxi = SilverServiceTaxi("Taxi", 100, 4)
    my_taxi.drive(60)
    print(my_taxi)


main()
