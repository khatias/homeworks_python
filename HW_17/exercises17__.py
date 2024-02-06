from datetime import datetime

class Car:
    __number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.__number_of_cars += 1

  
    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


    @classmethod
    def total_cars(cls):
        return cls.__number_of_cars


    def age_of_car(self):
        age = datetime.now().year - self.year
        print(f"{self.brand} {self.model} is {age} years old.")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def electric_car(self):    
        print(f"The battery life of this car is {self.battery_life} hour")


# ==================
car1 = Car(brand="Toyota", model="Camry", year=2022)
car2 = Car(brand="Honda", model="Civic", year=2023)
electric_car = ElectricCar(brand="Tesla", model="Model S", year=2022, battery_life=8)
car1.car_info()
car1.age_of_car()
electric_car.electric_car()

print("Total number of cars:", Car.total_cars())
print("Total number of cars:", car1.total_cars())
