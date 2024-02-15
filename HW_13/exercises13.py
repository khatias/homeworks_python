
chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]


import os
import json

def create_json_file(path, file_name):
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = f"{path}/{file_name}.json"

    try:
        with open(file_path, mode='x', encoding='utf-8'):
            print(f"File '{file_path}' created successfully.")
    except FileExistsError:
        print(f"File '{file_path}' already exists.")
    return file_path

file_path = create_json_file('files', 'chess_players')

def write_data_into_json_file(path, json_data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=2)

write_data_into_json_file(file_path, chess_players)        

def read_json_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

read_data = read_json_file(file_path)
print(read_data)

def update_json_file(path, new_data):
    existing_data = read_json_file(path) or []
    existing_data.extend(new_data)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=2)
        print(f"File '{path}' updated successfully.")

new_players = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

update_json_file(file_path, new_players)


updated_data = read_json_file(file_path)
print("\nUpdated Content:")
print(updated_data)







# 1.დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის მისამართს, სახელს და შემქნის მას.
# 2.დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს
# 3.დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს
# 4.დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს
# [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]
# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია
# import json