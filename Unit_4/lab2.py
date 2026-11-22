# Lab Exercise 2: Student Data Manager Using Text File

filename = "students.txt"

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Student name: ")
        roll = input("Roll number: ")

        with open(filename, "a") as file:
            file.write(f"{roll},{name}\n")

        print("Student saved.")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                print(file.read())

        except FileNotFoundError:
            print("No student records yet.")

    elif choice == "3":
        break

    else:
        print("Invalid choice")