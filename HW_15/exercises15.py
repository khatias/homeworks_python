# შექმენით csv ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,marks
# 1,string,0,string,string,0
# 2,string,0,string,string,0

# 1.დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას (id,name,age,grade,subject_name,marks) და თქვენ სტუდენტს დაამატებთ csv ფაილში.
# 2.დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.
# 3.დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის აიდს, საგანს და განახლებულ ქულას.

import os
import csv

def create_csv_file(file_path):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'age', 'grade', 'subject_name', 'marks'])

create_csv_file("students.csv")

def add_student_to_csv(id, name, age, grade, subject_name, marks):
    with open('students.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, age, grade, subject_name, marks])

new_id = int(input("Enter student ID: "))
new_name = input("Enter student name: ")
new_age = int(input("Enter student age: "))
new_grade = input("Enter student grade: ")
new_subject_name = input("Enter subject name: ")
new_marks = int(input("Enter student marks: "))


add_student_to_csv(new_id, new_name, new_age, new_grade, new_subject_name, new_marks)


def read_all_students():
    with open('students.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)

read_all_students()

def read_specific_student(student_id):
    with open('students.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['id']) == student_id:
                print(row)

read_specific_student(2)



def update_student_score():
    student_id = int(input("Enter student ID to update score: "))
    subject_name = input("Enter subject name: ")
    updated_score = int(input("Enter updated score: "))

    rows = []
    updated = False

    with open('students.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['id']) == student_id and row['subject_name'] == subject_name:
                row['grade'] = updated_score
                updated = True
            rows.append(row)

    if not updated:
        print(f"Student with ID {student_id} and subject {subject_name} not found.")
        return

    with open('students.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'marks']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Score for Student ID {student_id}, Subject {subject_name} updated successfully.")


update_student_score()
