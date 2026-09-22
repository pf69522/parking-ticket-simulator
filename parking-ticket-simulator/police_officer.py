"""Defines the PoliceOfficer class."""

from parking_ticket import ParkingTicket


class PoliceOfficer:
    """Represents a police officer who checks parked cars."""

    def __init__(self, name, badge_number):
        """Initialize a police officer."""
        self.name = name
        self.badge_number = badge_number

    def inspect(self, car, meter):
        """
        Inspect a parked car and its parking meter.

        Args:
            car: The ParkedCar object being inspected.
            meter: The ParkingMeter object for the car.

        Returns:
            A ParkingTicket if the car is illegally parked.
            Otherwise, returns None.
        """
        if car.minutes_parked <= meter.minutes_purchased:
            return None

        illegal_minutes = car.minutes_parked - meter.minutes_purchased

        return ParkingTicket(
            car,
            self.name,
            self.badge_number,
            illegal_minutes
        )