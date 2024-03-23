
import unittest
from vehicle import Vehicle, ElectricVehicle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("Toyota", "Camry", 2022)

    def test_fuel_up(self):
        self.assertEqual(self.vehicle.fuel_up, "Gas tank is now full or can move.")

    def test_drive(self):
        self.assertEqual(self.vehicle.drive, "The Camry is now driving.")

class TestElectricVehicle(unittest.TestCase):
    def setUp(self):
        self.electric_vehicle = ElectricVehicle("Tesla", "Model S", 2022)

    def test_charge(self):
        self.assertEqual(self.electric_vehicle.charge, "The vehicle is now charged.")

    def test_fuel_up(self):
        self.assertEqual(self.electric_vehicle.fuel_up, "This vehicle has no fuel tank!")

if __name__ == "__main__":
    unittest.main()