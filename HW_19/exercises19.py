# 1. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.

# 2. Car კლასს დაუმატეთ თითეული ატრიბუტისთვის set და get ფუნქციები მათი ცვლილებებისთვის.

# 3. დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის ინტეგერი და ასე შემდეგ.
class Car:
    valid_brands = {"Toyota", "Honda", "Ford", "Chevrolet"}  
    valid_models = {"Camry", "Accord", "F-150", "Silverado"} 

    def __new__(cls, *args, **kwargs):
        print("Creating instance using __new__ method")
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        print("Initializing instance using __init__ method")
        self._brand = None
        self._model = None
        self._year = None
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

    def set_brand(self, brand):
        if brand in self.valid_brands:
            self._brand = brand
        else:
            raise ValueError(f"Invalid brand: {brand}")

    def get_brand(self):
        return self._brand

    def set_model(self, model):
        if model in self.valid_models:
            self._model = model
        else:
            raise ValueError(f"Invalid model: {model}")

    def get_model(self):
        return self._model

    def set_year(self, year):
        if isinstance(year, int) and year > 0:
            self._year = year
        else:
            raise ValueError("Year must be a positive integer")

    def get_year(self):
        return self._year



try:
    car = Car("Toyota", "Camry", 2022)
    print(f"Brand: {car.get_brand()}")
    print(f"Model: {car.get_model()}")
    print(f"Year: {car.get_year()}")
except ValueError as e:
    print(e)
