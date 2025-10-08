students = []  # Empty list to store student details

# Accept student details
def accept():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    marks = input("Enter Marks: ")
    students.append([name, roll, marks])
    print("Student Added!\n")

# Display all students
def display():
    if not students:
        print("No Records Found!\n")
    else:
        print("\nName\tRoll No\tMarks")
        for s in students:
            print(f"{s[0]}\t{s[1]}\t{s[2]}")
        print()

# Search student by Roll No
def search():
    roll = input("Enter Roll No to Search: ")
    for s in students:
        if s[1] == roll:
            print(f"Found → Name: {s[0]}, Roll No: {s[1]}, Marks: {s[2]}\n")
            return
    print("Student Not Found!\n")

# Delete student by Roll No
def delete():
    roll = input("Enter Roll No to Delete: ")
    for s in students:
        if s[1] == roll:
            students.remove(s)
            print("Student Deleted!\n")
            return
    print("Student Not Found!\n")

# Update student marks
def update():
    roll = input("Enter Roll No to Update: ")
    for s in students:
        if s[1] == roll:
            marks = input("Enter New Marks: ")
            s[2] = marks
            print("Student Updated!\n")
            return
    print("Student Not Found!\n")

# Menu
while True:
    print("1. Accept\n2. Display\n3. Search\n4. Delete\n5. Update\n6. Exit")
    choice = input("Enter Choice: ")

    if choice == '1':
        accept()
    elif choice == '2':
        display()
    elif choice == '3':
        search()
    elif choice == '4':
        delete()
    elif choice == '5':
        update()
    elif choice == '6':
        print("Exiting Program... Goodbye!")
        break
    else:
        print("Invalid Choice!\n")