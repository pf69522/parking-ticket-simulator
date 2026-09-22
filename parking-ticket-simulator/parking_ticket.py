"""Defines the ParkingTicket class."""

import math


class ParkingTicket:
    """Represents a ticket issued to an illegally parked car."""

    def __init__(self, car, officer_name, badge_number, illegal_minutes):
        """Initialize a parking ticket."""
        self._car = car
        self.officer_name = officer_name
        self.badge_number = badge_number
        self.illegal_minutes = illegal_minutes

    @property
    def illegal_minutes(self):
        """Return the number of illegal parking minutes."""
        return self._illegal_minutes

    @illegal_minutes.setter
    def illegal_minutes(self, value):
        """Set the number of illegal parking minutes."""
        if not isinstance(value, int):
            raise TypeError("Illegal minutes must be an integer.")
        if value <= 0:
            raise ValueError("Illegal minutes must be greater than zero.")

        self._illegal_minutes = value

    @property
    def fine(self):
        """Calculate and return the parking fine."""
        hours = math.ceil(self.illegal_minutes / 60)

        return 25 + (hours - 1) * 10

    @property
    def car_make(self):
        """Return the car make."""
        return self._car.make

    @property
    def car_model(self):
        """Return the car model."""
        return self._car.model

    @property
    def car_color(self):
        """Return the car color."""
        return self._car.color

    @property
    def license_number(self):
        """Return the car license number."""
        return self._car.license_number

    def __str__(self):
        """Return a readable parking ticket report."""
        return (
            "Parking Ticket\n"
            f"Make: {self.car_make}\n"
            f"Model: {self.car_model}\n"
            f"Color: {self.car_color}\n"
            f"License Number: {self.license_number}\n"
            f"Illegal Minutes: {self.illegal_minutes}\n"
            f"Fine: ${self.fine}\n"
            f"Officer: {self.officer_name}\n"
            f"Badge Number: {self.badge_number}"
        )