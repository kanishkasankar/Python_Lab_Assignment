# Lab Exercise 1: Contact Book Using List and Dictionary
contacts = {}

while True:
    print("\\n1. Add contact  2. Search  3. Display all  4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone number: ")
        contacts[name] = phone
        print("Contact saved.")
    elif choice == "2":
        name = input("Search name: ")
        print("Phone:", contacts.get(name, "Contact not found"))
    elif choice == "3":
        for name, phone in contacts.items():
            print(name, ":", phone)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
