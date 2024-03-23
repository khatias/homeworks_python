import unittest
from vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("Toyota", "Camry", 2022)

    def test_fuel_up(self):
        self.assertEqual(self.vehicle.fuel_up, "Gas tank is now full or can move.")

    def test_drive(self):
        self.assertEqual(self.vehicle.drive, "The Camry is now driving.")

if __name__ == "__main__":
    unittest.main()
