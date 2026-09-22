"""Unit tests for the ParkedCar class."""

import unittest
from parked_car import ParkedCar


class TestParkedCar(unittest.TestCase):
    """Tests for the ParkedCar class."""

    def test_valid_construction(self):
        """Test creating a car with valid information."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 30)

        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.color, "Blue")
        self.assertEqual(car.license_number, "ABC123")
        self.assertEqual(car.minutes_parked, 30)

    def test_valid_reassignment(self):
        """Test assigning valid values to properties."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 30)

        car.make = "Honda"
        car.model = "Civic"
        car.color = "Red"
        car.license_number = "XYZ789"
        car.minutes_parked = 60

        self.assertEqual(car.make, "Honda")
        self.assertEqual(car.model, "Civic")
        self.assertEqual(car.color, "Red")
        self.assertEqual(car.license_number, "XYZ789")
        self.assertEqual(car.minutes_parked, 60)

    def test_empty_make(self):
        """Test that an empty make is rejected."""
        with self.assertRaises(ValueError):
            ParkedCar("", "Camry", "Blue", "ABC123", 30)

    def test_incorrect_make_type(self):
        """Test that a non-string make is rejected."""
        with self.assertRaises(TypeError):
            ParkedCar(123, "Camry", "Blue", "ABC123", 30)

    def test_zero_minutes_parked(self):
        """Test that zero parked minutes is valid."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 0)
        self.assertEqual(car.minutes_parked, 0)

    def test_negative_minutes_parked(self):
        """Test that negative parked minutes are rejected."""
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Camry", "Blue", "ABC123", -1)

    def test_noninteger_minutes_parked(self):
        """Test that noninteger parked minutes are rejected."""
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", "Blue", "ABC123", 30.5)


if __name__ == "__main__":
    unittest.main()