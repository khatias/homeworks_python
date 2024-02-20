# შექმენით ორი კლასი:
# I. Student, ატრიბუტებით: name, mark, address, სტატიკური ატრიბუტი row_id
# II. Address, ატრიბუტებით: city, street


# Student კლასის address ატრიბუტს მნიშვნელობად უნდა მიანჭოთ Address კლასის ეგზემპლარი.

# შექმენთ ორივე კლასის რამდენინე ეგზემპლარი.

# json მოდულის დახმარებით ფაილში შეინახეთ სტუდენტები.

# მოახდინეთ წაკითხვა. შეცვალეთ ატრიბუტ(ებ)ის მნიშვნელობა (მაგ.mark, str), დაამატეთ ახალი ატრიბუტი grade 
# მნიშვნელობით A, B, C, D (A -> [91-100], B -> [81-90], C -> [71-80], D -> <=70).

# შეცვლილი მონაცემები შეინახეთ ფაილში.


import json
import os

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Student:
    row_id = 0

    def __init__(self, name, mark, address):
        self.name = name
        self.mark = mark
        self.address = address
        self.grade = self.calculate_grade(mark)
        Student.row_id += 1
        self.row_id = Student.row_id 

    def calculate_grade(self, mark):
        if mark >= 91:
            return 'A'
        elif mark >= 81:
            return 'B'
        elif mark >= 71:
            return 'C'
        elif mark >= 61:
            return 'D'
        else:
            return 'F'

address1 = Address("Tbilisi", "Saburtalo street")
student1 = Student("Khatia", 90, address1)
address2 = Address("Tbilisi", "Nutsubidze street")
student2 = Student("Levan", 85, address2)
address3 = Address("Tbilisi", "Chavchavadze street")
student3 = Student("Mariam", 85, address3)
address4 = Address("Nika", "Kazbegi street")
student4 = Student("Sandro", 85, address4)

data = {
    "students": [
        {"row_id": student1.row_id, "name": student1.name, "mark": student1.mark, "address": {"city": student1.address.city, "street": student1.address.street}, "grade": student1.grade},
        {"row_id": student2.row_id, "name": student2.name, "mark": student2.mark, "address": {"city": student2.address.city, "street": student2.address.street}, "grade": student2.grade},
        {"row_id": student3.row_id, "name": student3.name, "mark": student3.mark, "address": {"city": student3.address.city, "street": student3.address.street}, "grade": student3.grade},
        {"row_id": student4.row_id, "name": student4.name, "mark": student4.mark, "address": {"city": student4.address.city, "street": student4.address.street}, "grade": student4.grade}
    ],
}

file_path = os.path.join("HW_21", "data.json")
os.makedirs("HW_21", exist_ok=True)

with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)


with open(file_path, "r") as json_file:
    data = json.load(json_file)


new_address = Address("Batumi", "Chavchavadze Street")
data["students"][0]["address"]["city"] = new_address.city
data["students"][0]["address"]["street"] = new_address.street


with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Address updated and data saved to data.json")





