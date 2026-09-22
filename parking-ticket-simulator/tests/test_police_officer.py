
"""Unit tests for the PoliceOfficer class."""

import unittest
from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


class TestPoliceOfficer(unittest.TestCase):
    """Tests for the PoliceOfficer class."""

    def test_car_under_purchased_time(self):
        """Test that no ticket is issued when time remains."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 30)
        meter = ParkingMeter(60)
        officer = PoliceOfficer("John Smith", "1234")

        ticket = officer.inspect(car, meter)

        self.assertIsNone(ticket)

    def test_car_exactly_at_purchased_time(self):
        """Test that no ticket is issued when time exactly matches."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 60)
        meter = ParkingMeter(60)
        officer = PoliceOfficer("John Smith", "1234")

        ticket = officer.inspect(car, meter)

        self.assertIsNone(ticket)

    def test_one_minute_over_creates_ticket(self):
        """Test that one illegal minute creates a ticket."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 61)
        meter = ParkingMeter(60)
        officer = PoliceOfficer("John Smith", "1234")

        ticket = officer.inspect(car, meter)

        self.assertIsNotNone(ticket)

    def test_illegal_minutes_calculated_correctly(self):
        """Test that illegal parking minutes are calculated correctly."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 90)
        meter = ParkingMeter(60)
        officer = PoliceOfficer("John Smith", "1234")

        ticket = officer.inspect(car, meter)

        self.assertEqual(ticket.illegal_minutes, 30)

    def test_ticket_contains_correct_information(self):
        """Test that the returned ticket contains correct information."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 90)
        meter = ParkingMeter(60)
        officer = PoliceOfficer("John Smith", "1234")

        ticket = officer.inspect(car, meter)

        self.assertEqual(ticket.car_make, "Toyota")
        self.assertEqual(ticket.license_number, "ABC123")
        self.assertEqual(ticket.officer_name, "John Smith")
        self.assertEqual(ticket.badge_number, "1234")