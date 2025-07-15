import json
import os


FILE_NAME = "phonebook.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)  # returns a dictionary
    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)
    print("Contacts saved successfully!")


def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    contacts[name] = phone
    print(f" Contact '{name}' added!")


def view_contacts(contacts):
    if not contacts:
        print(" No contacts found.")
    else:
        print("\n Your Contacts:")
        for name, phone in contacts.items():
            print(f" {name} : {phone}")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"Found: {name} -> {contacts[name]}")
    else:
        print(" Contact not found.")

#  Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f" Contact '{name}' deleted.")
    else:
        print(" Contact not found.")


def phonebook_app():
    contacts = load_contacts()
    
    while True:
        print("\n Phonebook Menu:")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Delete Contact")
        print("5️⃣ Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print(" Exiting Phonebook... Bye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    phonebook_app()
