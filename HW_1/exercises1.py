


# 1. დაწერეთ პროგრამა რომელიც input მეთოდის საშუალებით მიიღებს 2 რიცხვს და დააბრუნებს ამ რიცხვებს შორის შესრულებული არითმეტიკული ოპერაციების შედეგებს (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება).

num1 = eval(input("Enter first number "))
num2 = eval(input("Enter second number "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")

# 2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

d1 = eval(input("Enter the length of the first diagonal: "))
d2 = eval(input("Enter the length of the second diagonal: "))

area = d1 * d2 / 2
print(f"The area of the rhombus  is: {area}")
# 3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში.

meters = eval(input("Enter the number of meters: "))
centimeters = meters * 100
decimeters = meters * 10
millimeters = meters * 1000
miles = meters / 1609.34

print(f"{meters} meter is {centimeters} centimeters.")
print(f"{meters} meter is {decimeters} decimeters.")
print(f"{meters} meter is {millimeters} millimeters.")
print(f"{meters} meter is {miles} miles.")

# 4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.

height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area_of_triangle = (base / 2) * height
print(f"The area of the triangle is: {area_of_triangle}")