"""Defines the PoliceOfficer class."""

from parking_ticket import ParkingTicket


class PoliceOfficer:
    """Represents a police officer who checks parked cars."""

    def __init__(self, name, badge_number):
        """Initialize a police officer."""
        self.name = name
        self.badge_number = badge_number

    def inspect(self, car, meter):
        """Inspect a parked car and return a ticket if needed."""
        if car.minutes_parked <= meter.minutes_purchased:
            return None

        illegal_minutes = car.minutes_parked - meter.minutes_purchased

        return ParkingTicket(
            car,
            self.name,
            self.badge_number,
            illegal_minutes
        )