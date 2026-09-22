"""Demonstrates the Parking Ticket Simulator."""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def main():
    """Run a demonstration of the parking ticket simulator."""

    car = ParkedCar(
        "Toyota",
        "Camry",
        "Blue",
        "ABC123",
        90
    )

    meter = ParkingMeter(60)

    officer = PoliceOfficer(
        "John Smith",
        "1234"
    )

    ticket = officer.inspect(car, meter)

    if ticket is not None:
        print(ticket)
    else:
        print("No parking violation.")


if __name__ == "__main__":
    main()
