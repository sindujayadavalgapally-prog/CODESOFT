contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added!")

    elif choice == "2":
        for name, details in contacts.items():
            print(name, details)

    elif choice == "3":
        name = input("Enter Name: ")

        if name in contacts:
            print(contacts[name])
        else:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted")
        else:
            print("Contact Not Found")

    elif choice == "5":
        break

    else:
        print("Invalid Choice")contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added!")

    elif choice == "2":
        for name, details in contacts.items():
            print(name, details)

    elif choice == "3":
        name = input("Enter Name: ")

        if name in contacts:
            print(contacts[name])
        else:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted")
        else:
            print("Contact Not Found")

    elif choice == "5":
        break

    else:
        print("Invalid Choice")
