import pytest
from vehicle import Vehicle, ElectricVehicle

@pytest.fixture
def vehicle():
    return Vehicle("Toyota", "Corolla", 2023)

@pytest.fixture
def electric_vehicle():
    return ElectricVehicle("Nissan", "Leaf", 2024)

def test_vehicle_creation(vehicle):
    assert vehicle.brand == "Toyota"
    assert vehicle.model == "Corolla"
    assert vehicle.year == 2023

def test_electric_vehicle_creation(electric_vehicle):
    assert electric_vehicle.brand == "Nissan"
    assert electric_vehicle.model == "Leaf"
    assert electric_vehicle.year == 2024

def test_fuel_up(vehicle):
    assert vehicle.fuel_up == "Gas tank is now full or can move."

def test_drive(vehicle):
    assert vehicle.drive == "The Corolla is now driving."

def test_charge(electric_vehicle):
    assert electric_vehicle.charge == "The vehicle is now charged."

def test_fuel_up_for_electric_vehicle(electric_vehicle):
    assert electric_vehicle.fuel_up == "This vehicle has no fuel tank!"

if __name__ == "__main__":
    pytest.main()
