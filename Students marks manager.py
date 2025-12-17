students = []

def add_students():
    name = input("Enter student name :")
    marks = int(input("Enter marks: "))
    students.append({"name ": name, "marks ": marks })
    print("Student added successfully")

def view_students():
    if not students:      #to check if list is empty
        print("No students data found. ")

    else:
        for i in range(len(students)):
            print(i+1,students[i]["name"],"-",students[i]["marks"])

def menu():
    print("\n1. Add student")
    print("2. View Student")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice =="1":
        add_students()
    elif choice =="2":
        view_students()
    elif choice =="3":
        print("Exiting program")
        break
    else:
        print("Invalid choice")



   