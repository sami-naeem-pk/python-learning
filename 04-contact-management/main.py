"""
Contact Manager Project
A simple command-line application to add, view, delete, and persistently 
save contacts using JSON storage in Python.
"""

import json
import os

# Global dictionary to store contacts in memory.
# Format: {contact_id: {"name": "...", "phone": "..."}, ...}
contacts = {}

def load():
    """
    Loads saved contacts from 'contacts.json' when the program starts.
    If the file doesn't exist or is corrupted, it initializes an empty dictionary.
    """
    global contacts
    if os.path.exists("contacts.json"):
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)
                # Convert string keys back to integers since JSON keys are always strings
                contacts = {int(k): v for k, v in data.items()}
        except json.JSONDecodeError:
            # Handle cases where the JSON file is empty or corrupted
            contacts = {}

def add():
    """
    Prompts the user for a name and phone number, generates a unique ID,
    and adds the new contact to the dictionary.
    """
    name = input("Enter name: ")
    phone = input(f"Enter phone number for {name}: ")
    
    # Generate a unique contact ID by finding the max key, defaulting to 0 if empty, then adding 1
    contact_id = max(contacts.keys(), default=0) + 1
    
    contacts[contact_id] = {"name": name, "phone": phone}
    print("✓ Contact has been added!")
    

def view():
    """
    Displays all stored contacts in a formatted list.
    If no contacts exist, it notifies the user.
    """
    if not contacts:
        print("\n--- No contacts found! ---\n")
        return
        
    print("\n----- Contacts -----")
    for contact_id, info in contacts.items():
        print(f"{contact_id}. {info['name']} [{info['phone']}]")
    print("-------------------------\n")
    
def delete_contact():
    """
    Displays current contacts and prompts the user for a contact ID to delete.
    Includes error handling for invalid inputs or non-existent IDs.
    """
    view()
    if not contacts:
        return
        
    try:
        contact_id = int(input("Enter contact ID to delete: "))
        if contact_id in contacts:
            del contacts[contact_id]
            print("✓ Contact deleted successfully!")
        else:
            print("❌ Contact ID not found.")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")    
        
def save():
    """
    Saves the current dictionary of contacts to 'contacts.json' 
    using indentation for readability.
    """
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
        print("✓ Contacts saved to the file!")

# Load existing contacts immediately when the program runs
load()

# Main application loop
while True:
    print(" -----Contact-Manager-----")
    print(" 1. Add contact")
    print(" 2. View contacts")
    print(" 3. Delete contact")
    print(" 4. Exit")
    
    # Get user choice with error handling to prevent crashes on letters/symbols
    try:
        c = int(input("Enter 1, 2, 3, or 4: "))
    except ValueError:
        print("❌ Enter from 1, 2, 3, or 4:")
        continue
    
    # Route user choice to the appropriate function
    if c == 1:
        add()
    elif c == 2:
        view()
    elif c == 3:
        delete_contact()
    elif c == 4:
        save()            
        break
