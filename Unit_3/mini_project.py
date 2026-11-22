# Mini Project: Attendance Tracker
students = {}

while True:
    print("\\n1. Mark attendance  2. View attendance  3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Student name: ")
        status = input("Present or Absent (P/A): ").upper()
        if status in ("P", "A"):
            students[name] = "Present" if status == "P" else "Absent"
            print("Attendance recorded.")
        else:
            print("Enter P or A.")
    elif choice == "2":
        print("Attendance List")
        for name, status in students.items():
            print(name, "-", status)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
