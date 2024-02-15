# შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.

num_list =[44, 23, 11, 8, 20, 56, 33, 55]
number = 52
if number in num_list:
    print(f"{number} is in the list")
else:
    print(f"{number} is not in the list")
# დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.

number = 25

if number % 2 == 0:
    print(f"The {number} is even")
else:
    print(f"The {number} is odd")

# შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"
st1="hello"
st2="hello"
if st1 is st2:
    print("Same object")
else:
    print("Different object")

#     შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
# თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";

# თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";

# სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".

# რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.

# მაგ.:


num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = eval(input("Enter a number:"))

if num_list[2] < number < num_list[-1]:
    print("More than list elements")
elif number == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")