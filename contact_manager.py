import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, company, email, phone, category):
    contacts = load_contacts()
    contact = {
        "name": name,
        "company": company,
        "email": email,
        "phone": phone,
        "category": category
    }
    contacts.append(contact)
    save_contacts(contacts)

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found")
    for c in contacts:
        print(c)

def update_contact(name, new_data):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"] == name:
            contact.update(new_data)
    save_contacts(contacts)

def delete_contact(name):
    contacts = load_contacts()
    contacts = [c for c in contacts if c["name"] != name]
    save_contacts(contacts)

def search_contact(keyword):
    contacts = load_contacts()
    results = []
    for c in contacts:
        if keyword.lower() in c["name"].lower() or keyword.lower() in c["company"].lower():
            results.append(c)
    return results

def filter_by_category(category):
    contacts = load_contacts()
    return [c for c in contacts if c["category"].lower() == category.lower()]