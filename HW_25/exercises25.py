# TODO SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია

# Single Responsibility Principle
class BookDetails:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookPricing:
    def __init__(self, price):
        self.price = price
    
    def get_discounted_price(self, discount):
        return self.price * (1 - discount)


book_details = BookDetails("Title", "Author")
book_pricing = BookPricing(100)
discounted_price = book_pricing.get_discounted_price(0.2)
print(discounted_price)


# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle

from abc import ABC, abstractmethod

class Payment(ABC):
    """Abstract Payment class"""
    
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    """Credit Card Payment class"""
    
    def process_payment(self, amount):
        print(f"Processing credit card payment for ${amount}")

class PayPalPayment(Payment):
    """PayPal Payment class"""
    
    def process_payment(self, amount):
        print(f"Processing PayPal payment for ${amount}")


credit_card_payment = CreditCardPayment()
credit_card_payment.process_payment(100)

paypal_payment = PayPalPayment()
paypal_payment.process_payment(50)

# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def energy_source(self):
        pass

class ElectricCar(Vehicle):
    def energy_source(self):
         return "Battery capacity is 100 kWh"

class FuelCar(Vehicle):
    def energy_source(self):
       return "100 Liters"

electric_car = ElectricCar()
fuel_car = FuelCar()

print("Electric Car Energy Source:", electric_car.energy_source())
print("Fuel Car Energy Source:", fuel_car.energy_source())
    
# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle


from abc import ABC, abstractmethod

class AudioPlayer(ABC):
    @abstractmethod
    def play_audio(self):
        pass

class VideoPlayer(ABC):
    @abstractmethod
    def play_video(self):
        pass

# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)
    
from abc import ABC, abstractmethod

class Display(ABC):
    @abstractmethod
    def show(self, data):
        pass

class ConsoleDisplay(Display):
    def show(self, data):
        print(data)

class WeatherStation:
    def __init__(self, display):
        self.display = display

    def report(self):
        self.display.show("Weather Data")


