# 1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

int_list = [10, 20, 30, 40]

def add_to_int_list(number):
    global int_list
    int_list.append(number)


number_to_add = 50
add_to_int_list(number_to_add)

print("Updated int_list:", int_list)

# 2.დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].
def calculate_sum(numbers):
    return sum(numbers)


number_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result = calculate_sum(number_list)

print(f"The sum of the numbers is: {result}")

# 3.შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას

gl_str = "Global"

def create_local_variable():
    gl_str = "Local"
    return gl_str

local_value = create_local_variable()

print("Global variable:", gl_str)
print("Local variable:", local_value)

# 4.რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).

def sum_of_digits(number):

    if number < 10:
        return number
    else:
    
        return number % 10 + sum_of_digits(number // 10)

input_number = 12345
result = sum_of_digits(input_number)

print(f"The sum of the digits in {input_number} is: {result}")

# 5.რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)

def reverse_string(s):

    if len(s) <= 1:
        return s

    else:
        return reverse_string(s[1:]) + s[0]


input_string = "Hello"
output_string = reverse_string(input_string)
print(output_string)

