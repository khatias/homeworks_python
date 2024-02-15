# 1.დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

def group_lists(list1, list2):
    zipped_lists = zip(list1, list2)
    result_list = list(zipped_lists)
    return result_list

output = group_lists([1, 2, 3], ['a', 'b', 'c'])
print(output)

# 2.დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.

# params:[1, 2, 3, 4, 5] 
# output: 120

from functools import reduce
def multiply_elements(numbers):
    try:
        if all(isinstance(num, (int, float)) for num in numbers):
            result = reduce(lambda x, y: x * y, numbers)
            return result
        else:
            raise TypeError("Error: Input must be a list of numbers.")
    except TypeError as exception:
        return str(exception)

input_numbers = [1, 2, 3, 4, 5]
output = multiply_elements(input_numbers)
print(output)


# 3.დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

def only_odd(numbers):
    filter_odd = lambda x: x % 2 != 0
    odd_elements = list(filter(filter_odd, numbers))
    return odd_elements

numbers = [1, 2, 3, 4, 5, 6, 7]
result = only_odd(numbers)
print(result)

# 4.დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. 
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']

def filter_strings_by_suffix(string_list, suffix):
    try:
        if all(isinstance(s, str) for s in string_list):
            filtered_list = list(filter(lambda x: x.endswith(suffix), string_list))
            return filtered_list
        else:
            raise TypeError("Input must be a list of strings.")
    except TypeError as exception:
        return f"Error: {exception}"

string_list = ['hello', 'world', 'coding', 'nod']
suffix = 'ing'
output = filter_strings_by_suffix(string_list, suffix)
print(output)


