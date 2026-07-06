import csv
import os



USERNAME = "nihuu"
PASSWORD = "1234"

print("========== STUDENT MANAGEMENT SYSTEM ==========\n")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username != USERNAME or password != PASSWORD:
    print("Invalid Username or Password!")
    exit()

print("\nLogin Successful!")

if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Course", "Phone"])




def add_student():

    sid = input("Enter Student ID: ")

    
    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] == sid:
                print("Student ID already exists!")
                return

    name = input("Enter Name: ")
    while True:
      age = input("Enter Age: ")

      if age.isdigit() and 16 <= int(age) <= 100:
        break

    print("Invalid Age! Enter age between 16 and 100.")
    course = input("Enter Course: ")
    while True:
      phone = input("Enter Phone Number: ")

      if phone.isdigit() and len(phone) == 10:
        break

    print("Phone number must contain exactly 10 digits.")

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, age, course, phone])

    print("\nStudent Added Successfully!")


# ---------------- DISPLAY STUDENTS ----------------

def display_students():

    with open("students.csv", "r") as file:

        reader = csv.reader(file)

        print("\n{:<10}{:<20}{:<10}{:<20}{:<15}".format("ID","Name","Age","Course","Phone"))
        print("-"*75)

        for row in reader:
            print("{:<10}{:<20}{:<10}{:<20}{:<15}".format(*row))


# ---------------- SEARCH STUDENT ----------------

def search_student():

    sid = input("Enter Student ID: ")

    found = False

    with open("students.csv","r") as file:

        reader = csv.reader(file)

        for row in reader:

            if row[0] == sid:

                print("\nStudent Found")
                print("ID :",row[0])
                print("Name :",row[1])
                print("Age :",row[2])
                print("Course :",row[3])
                print("Phone :",row[4])

                found = True
                break

    if not found:
        print("Student Not Found")


# ---------------- UPDATE STUDENT ----------------

def update_student():

    sid = input("Enter Student ID to Update: ")

    rows = []

    found = False

    with open("students.csv","r") as file:

        reader = csv.reader(file)

        for row in reader:

            if row[0] == sid:

                print("Enter New Details")

                row[1] = input("Name : ")
                row[2] = input("Age : ")
                row[3] = input("Course : ")
                row[4] = input("Phone : ")

                found = True

            rows.append(row)

    with open("students.csv","w",newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)

    if found:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found")


# ---------------- DELETE STUDENT ----------------

def delete_student():

    sid = input("Enter Student ID to Delete: ")

    rows = []

    found = False

    with open("students.csv","r") as file:

        reader = csv.reader(file)

        for row in reader:

            if row[0] == sid:
                found = True
                continue

            rows.append(row)

    with open("students.csv","w",newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)

    if found:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found")
# ---------------- TOTAL STUDENTS ----------------

def total_students():

    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        count = -1

        for row in reader:
            count += 1

    print(f"\nTotal Students : {count}")


# ---------------- SEARCH BY NAME ----------------

def search_by_name():

    name = input("Enter Student Name: ")

    found = False

    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[1].lower() == name.lower():

                print("\nStudent Found")
                print("ID :", row[0])
                print("Name :", row[1])
                print("Age :", row[2])
                print("Course :", row[3])
                print("Phone :", row[4])

                found = True

    if not found:
        print("Student Not Found")

while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Search Student by Name")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
      add_student()

    elif choice == "2":
       display_students()


    elif choice == "3":
       search_student()

    elif choice == "4":
       update_student()

    elif choice == "5":
       delete_student()
 
    elif choice == "6":
       total_students()
 
    elif choice == "7":
       search_by_name()

    elif choice == "8": 
       print("Thank You!")
       break

    else:
       print("Invalid Choice!")