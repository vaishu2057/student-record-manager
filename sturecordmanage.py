def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{branch},{marks}\n")

    print("✅ Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("⚠️ No student records found.")
                return
            print("\nRoll\tName\tBranch\tMarks")
            print("----------------------------------")
            for line in data:
                record = line.strip().split(",")
                print("\t".join(record))
    except FileNotFoundError:
        print("⚠️ No records found. Add some students first!")


def search_student():
    roll_to_search = input("Enter Roll Number to Search: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                if line.startswith(roll_to_search + ","):
                    print("✅ Student Found: ", line.strip())
                    found = True
                    break
        if not found:
            print("❌ Student not found.")
    except FileNotFoundError:
        print("⚠️ No data file found.")


def delete_student():
    roll_to_delete = input("Enter Roll Number to Delete: ")
    lines = []

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            for line in lines:
                if not line.startswith(roll_to_delete + ","):
                    file.write(line)

        print("✅ Student deleted (if existed).")
    except FileNotFoundError:
        print("⚠️ No data file found.")


def update_student():
    roll_to_update = input("Enter Roll Number to Update: ")
    updated = False
    lines = []

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            for line in lines:
                if line.startswith(roll_to_update + ","):
                    print("Enter new details:")
                    name = input("New Name: ")
                    branch = input("New Branch: ")
                    marks = input("New Marks: ")
                    file.write(f"{roll_to_update},{name},{branch},{marks}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("✅ Student updated.")
        else:
            print("❌ Student not found.")
    except FileNotFoundError:
        print("⚠️ No data file found.")


# 🔁 Main Menu Loop
while True:
    print("\n==============================")
    print("🎓 Student Record Management")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        update_student()
    elif choice == '6':
        print("👋 Exiting the application. Goodbye!")
        break
    else:
        print("❗ Invalid choice. Please try again.")
