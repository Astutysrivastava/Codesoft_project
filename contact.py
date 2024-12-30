class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        """Add a new contact."""
        print("\nAdd New Contact:")
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email Address: ").strip()
        address = input("Enter Address: ").strip()

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        print(f"Contact for {name} added successfully!")

    def view_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("\nNo contacts available.")
            return
        
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        query = input("\nEnter Name or Phone Number to Search: ").strip()
        found_contacts = [
            contact for contact in self.contacts
            if query.lower() in contact['name'].lower() or query in contact['phone']
        ]

        if not found_contacts:
            print("No contacts found.")
        else:
            print("\nSearch Results:")
            for contact in found_contacts:
                self.display_contact(contact)

    def update_contact(self):
        """Update an existing contact."""
        query = input("\nEnter Name or Phone Number of the Contact to Update: ").strip()
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                print("\nContact Found:")
                self.display_contact(contact)
                
                print("\nEnter new details (leave blank to keep existing):")
                contact['name'] = input(f"Name [{contact['name']}]: ") or contact['name']
                contact['phone'] = input(f"Phone [{contact['phone']}]: ") or contact['phone']
                contact['email'] = input(f"Email [{contact['email']}]: ") or contact['email']
                contact['address'] = input(f"Address [{contact['address']}]: ") or contact['address']
                print("Contact updated successfully!")
                return
        print("No matching contact found.")

    def delete_contact(self):
        """Delete a contact."""
        query = input("\nEnter Name or Phone Number of the Contact to Delete: ").strip()
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                print("\nContact Found:")
                self.display_contact(contact)
                confirm = input("Are you sure you want to delete this contact? (yes/no): ").lower()
                if confirm == "yes":
                    self.contacts.remove(contact)
                    print("Contact deleted successfully!")
                else:
                    print("Deletion canceled.")
                return
        print("No matching contact found.")

    def display_contact(self, contact):
        """Display contact details."""
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

    def menu(self):
        """Display the main menu and handle user input."""
        while True:
            print("\n--- Contact Management System ---")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ").strip()
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Exiting Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()
