# 1.დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(n + 1):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence


n = 10  
result = generate_fibonacci(n)
print(result)

# 2.დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები.
# (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.

def are_anagrams(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


string1 = "race"
string2 = "care"
result = are_anagrams(string1, string2)

if result:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")

# # 3.დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5 
result = factorial(number)
print(f"The factorial of {number} is: {result}")


# # 4.დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.
def count_char_occurrences(input_string, target_char):
    count = 0
    for char in input_string:
        if char == target_char:
            count += 1
    return count


input_str = "hello world"
target_character = "l"
result = count_char_occurrences(input_str, target_character)

print(f"The character '{target_character}' appears {result} times in the string.")
