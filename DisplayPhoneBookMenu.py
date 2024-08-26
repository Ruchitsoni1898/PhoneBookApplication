phonebook = {}


# Display the phonebook menu
def display_phonebook():
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")


# Add a new contact
def add_contact():
    name = input("Enter New Contact Name: ")
    if name in phonebook:
        print("Contact already exists!")
    else:
        phone_number = input("Add Phone Number: ")
        phonebook[name] = phone_number
        print(f"Contact {name} has been added to the phonebook.")


# Search for a contact
def search_contact():
    search_name = input("Enter Contact Name to Search: ")
    if search_name in phonebook:
        print(f"{search_name}: {phonebook[search_name]}")
    else:
        print("Contact details not found.")


# Update a contact's number
def update_contact():
    update_name = input("Enter Contact Name to Update: ")
    if update_name in phonebook:
        new_number = input("Enter New Number: ")
        phonebook[update_name] = new_number
        print(f"Contact {update_name} has been updated in the phonebook.")
    else:
        print("Contact not found.")


# Delete a contact
def delete_contact():
    delete_name = input("Enter Contact Name to Delete: ")
    if delete_name in phonebook:
        del phonebook[delete_name]
        print(f"Contact {delete_name} has been deleted from the phonebook.")
    else:
        print("Contact not found.")


# View all contacts
def view_all_contacts():
    if not phonebook:
        print("The phonebook is empty.")
    else:
        print("\nPhonebook Contact List:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")


# Main app function
def phone_book_app():
    while True:
        display_phonebook()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            view_all_contacts()
        elif choice == '6':
            print("Exiting phonebook.")
            break
        else:
            print("Invalid option, please try again.")


phone_book_app()
