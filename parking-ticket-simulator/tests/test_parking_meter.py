"""Unit tests for the ParkingMeter class."""

import unittest
from parking_meter import ParkingMeter


class TestParkingMeter(unittest.TestCase):
    """Tests for the ParkingMeter class."""

    def test_valid_construction(self):
        """Test creating a meter with valid purchased minutes."""
        meter = ParkingMeter(60)

        self.assertEqual(meter.minutes_purchased, 60)

    def test_zero_minutes(self):
        """Test that zero purchased minutes is valid."""
        meter = ParkingMeter(0)

        self.assertEqual(meter.minutes_purchased, 0)

    def test_valid_reassignment(self):
        """Test assigning valid purchased minutes."""
        meter = ParkingMeter(60)

        meter.minutes_purchased = 120

        self.assertEqual(meter.minutes_purchased, 120)

    def test_negative_minutes(self):
        """Test that negative purchased minutes are rejected."""
        with self.assertRaises(ValueError):
            ParkingMeter(-1)

    def test_noninteger_minutes(self):
        """Test that noninteger purchased minutes are rejected."""
        with self.assertRaises(TypeError):
            ParkingMeter(60.5)


if __name__ == "__main__":
    unittest.main()
