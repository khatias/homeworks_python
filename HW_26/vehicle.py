class Vehicle:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    self.gaz_tank_size = 45
    self.fuel_level = 0
  

  @property
  def fuel_up(self):
    self.fuel_level = self.gaz_tank_size

    if self.fuel_level:
      return "Gas tank is now full or can move."
    
    return "Gas tank is empty and can not move."
  

  @property
  def drive(self):
    return f"The {self.model} is now driving."


class ElectricVehicle(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)

    self.battery_size = 85
    self.charge_level = 0
  

  @property
  def charge(self):
    self.charge_level = 100

    return "The vehicle is now charged."
  

  @property
  def fuel_up(self):
    return "This vehicle has no fuel tank!"