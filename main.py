from contact_manager import *

while True:
    print("\n=== Client & Vendor Contact Management System ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Filter by Category")
    print("5. Update Contact")
    print("6. Delete Contact")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        company = input("Company: ")
        email = input("Email: ")
        phone = input("Phone: ")
        category = input("Category (Client/Vendor/Partner): ")
        add_contact(name, company, email, phone, category)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        keyword = input("Enter name/company to search: ")
        results = search_contact(keyword)
        for r in results:
            print(r)

    elif choice == "4":
        category = input("Enter category: ")
        results = filter_by_category(category)
        for r in results:
            print(r)

    elif choice == "5":
        name = input("Enter contact name to update: ")
        new_email = input("New Email: ")
        new_phone = input("New Phone: ")
        update_contact(name, {"email": new_email, "phone": new_phone})

    elif choice == "6":
        name = input("Enter contact name to delete: ")
        delete_contact(name)

    elif choice == "7":
        break