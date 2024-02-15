# 1.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

user_input = input("Enter a string: ")
encoded_string = user_input.encode('utf-8')
print(encoded_string)


# 2.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და დაუმატეთ ქვესტრიქონი 'Python'. თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.
# მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია .strip().

# მაგ.:

# "  Python is funny     ".strip()   ====>  "Python is funny"


user_input = input("Enter a string: ")

cleaned_str = user_input.strip().lower()

if "python" in cleaned_str:
    cleaned_str = cleaned_str.replace("python", "Python")
else:
    cleaned_str += ' Python'

print(cleaned_str)

# 3.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

user_input = input("Enter a string: ")
half_text = len(user_input) // 2

first_half = user_input[:half_text]
print("First Half:", first_half)

# 4.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება. სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)

import string 

digit_count = 0
contains_punctuation = False
user_input = input("Enter a string: ")

for char in user_input: 
    if char in string.punctuation: 
        contains_punctuation = True

    if char.isdigit(): 
        digit_count += 1

if digit_count == 1 and not contains_punctuation:
    print("The string is valid.")
else:
    print("The string is not valid.")

# 5.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.
import base64

user_input = input("Enter a string: ")
user_input = base64.b64encode(user_input.encode())
print(user_input)
user_input= base64.b64decode(user_input.decode())
print(user_input)