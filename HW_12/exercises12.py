"""TODO
დაწერეთ ფუნქცია რომელიც ტერმინალში მომხმარებელს გამოუტანს სტუდენტების აიდის (id) სიას,
მომხარებელი აირჩევს სტუდენტის აიდის, მიიღებული აიდისთვის დაბეჭდავს სტუდენტის მონაცემებს
მონაცემებში უნდა დაიბეჭდოს (სახელი, გვარი, ასაკი და ქულა თითოეული საგნის მიხედვით)

მაგალითად: მომხარებელმა თუ აირჩია სტუდენტი აიდით 20, უნდა დაბეჭდოთ ამ სტუდენტის ინფომრაცია

terminal ouput: 
studentebis ID: 20, 25, 100, 56, 1232, 846723
airchiet studentis ID: 
შემდეგ მომხარებელს შეყავს აიდი, მაგალითად  - 20 

თქვენ ბეჭდავთ ტერმინალში შემდეგ ინფორმაციას output:

student infomration:
ID: 20, name: Giorgi, age: 25
subject: Math, grade: B
subject: Physics, grade: A
subject: English, grade: A
subject: Chemistry, grade: B
subject: History, grade: c

""" 
my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

def print_student_info(my_dict, selected_id):
    student_ids = [student["id"] for student in my_dict["students"]]

    
    if selected_id in student_ids:
        print("student's ID: " + ", ".join(map(str, student_ids)))
        print(f"Selected Student ID: {selected_id}")
        
        print("stundent  information:")   
        for student in my_dict["students"]:
            if student["id"] == selected_id:
                print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
                
        for subject in my_dict["subjects"]:
            grade = subject["grades"].get(str(selected_id), "N/A")
            print(f"subject: {subject['name']}, grade: {grade}")
    else:
        print("Invalid student ID. Please enter a valid ID.")

selected_id = int(input("Enter the student ID: "))
print_student_info(my_dict, selected_id)
