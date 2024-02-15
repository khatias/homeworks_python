# 1.დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.

n = eval(input("Enter the number: "))
sum= 0
for i in range(1, n):
    sum  += i
print("Sum of numbers:", sum)

# 2.დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1
n = eval(input("Enter the number: "))
while n > 0:
    print(n)
    n -= 1

#  3.დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი. როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.   
import random
secret_number = random.randint(1, 100)
your_guess = eval(input("Guess the number: "))

while your_guess != secret_number:
    if secret_number < your_guess:
        print("The number is high.")
    elif secret_number > your_guess:
        print("The number is low.")
    your_guess = eval(input("Guess the number: "))

print("You won! The secret number was", secret_number)

# 4.დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, შეამოწმეთ რიცხვი თუ დადებითია, 
# მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

total_sum = 0

while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == "sum":
        break

    if user_input.lstrip('-').isdigit():
        n = int(user_input)
        if n > 0:
            total_sum += n
        else:
            print("Please enter a positive number.")
    else:
        print("Invalid input. Please enter a valid numeric value.")

print("Total sum:", total_sum)
