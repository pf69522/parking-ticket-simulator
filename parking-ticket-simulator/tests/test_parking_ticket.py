"""Unit tests for the ParkingTicket class."""

import unittest
from parked_car import ParkedCar
from parking_ticket import ParkingTicket


class TestParkingTicket(unittest.TestCase):
    """Tests for the ParkingTicket class."""

    def setUp(self):
        """Create a car used by the ticket tests."""
        self.car = ParkedCar(
            "Toyota", "Camry", "Blue", "ABC123", 120
        )

    def test_one_illegal_minute(self):
        """Test the fine for one illegal minute."""
        ticket = ParkingTicket(self.car, "John Smith", "1234", 1)
        self.assertEqual(ticket.fine, 25)

    def test_sixty_illegal_minutes(self):
        """Test the fine for sixty illegal minutes."""
        ticket = ParkingTicket(self.car, "John Smith", "1234", 60)
        self.assertEqual(ticket.fine, 25)

    def test_sixty_one_illegal_minutes(self):
        """Test the fine for sixty-one illegal minutes."""
        ticket = ParkingTicket(self.car, "John Smith", "1234", 61)
        self.assertEqual(ticket.fine, 35)

    def test_one_hundred_twenty_illegal_minutes(self):
        """Test the fine for 120 illegal minutes."""
        ticket = ParkingTicket(self.car, "John Smith", "1234", 120)
        self.assertEqual(ticket.fine, 35)

    def test_one_hundred_twenty_one_illegal_minutes(self):
        """Test the fine for 121 illegal minutes."""
        ticket = ParkingTicket(self.car, "John Smith", "1234", 121)
        self.assertEqual(ticket.fine, 45)

    def test_car_information(self):
        """Test that the ticket contains correct car information."""
        ticket = ParkingTicket(self.car, "John Smith", "1234", 30)

        self.assertEqual(ticket.car_make, "Toyota")
        self.assertEqual(ticket.car_model, "Camry")
        self.assertEqual(ticket.car_color, "Blue")
        self.assertEqual(ticket.license_number, "ABC123")

    def test_officer_information(self):
        """Test that the ticket contains correct officer information."""
        ticket = ParkingTicket(self.car, "John Smith", "1234", 30)

        self.assertEqual(ticket.officer_name, "John Smith")
        self.assertEqual(ticket.badge_number, "1234")

    def test_ticket_report(self):
        """Test that the ticket report contains required information."""
        ticket = ParkingTicket(self.car, "John Smith", "1234", 30)

        report = str(ticket)

        self.assertIn("Toyota", report)
        self.assertIn("Camry", report)
        self.assertIn("Blue", report)
        self.assertIn("ABC123", report)
        self.assertIn("30", report)
        self.assertIn("25", report)
        self.assertIn("John Smith", report)
        self.assertIn("1234", report)