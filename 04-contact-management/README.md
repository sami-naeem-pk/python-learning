Contact Manager

A command-line Contact Management application built with Python. It allows users to add, view, and delete contacts while storing contact information in a JSON file for persistent storage.

Features

- Add Contacts: Save a contact's name and phone number.
- View Contacts: Display all saved contacts with their unique IDs.
- Delete Contacts: Remove contacts using their assigned IDs.
- Persistent Storage: Save contacts in a "contacts.json" file.
- Load Existing Data: Automatically load previously saved contacts when the program starts.
- Input Validation: Handle invalid menu choices and contact IDs.
- Error Handling: Handle corrupted or invalid JSON data.

Technologies Used

- Python 3
- "json" module
- "os" module

Python Concepts Practiced

- Functions and function calls
- Dictionaries and nested dictionaries
- Global variables
- File handling ("open()")
- JSON serialization and deserialization
- Exception handling ("try", "except")
- "ValueError" and "JSONDecodeError"
- Conditional statements ("if", "elif", "else")
- "while" and "for" loops
- Dictionary methods ("keys()", "items()")
- Dictionary operations (adding, accessing, and deleting entries)
- "max()" function
- Input validation
- f-strings

How to Run

1. Make sure Python 3 is installed on your computer.

2. Clone this repository:
   
   git clone https://github.com/sami-naeem-pk/python-learning.git

3. Navigate to the project directory:
   
   cd python-projects/04-contact-management

4. Run the program:
   
   python main.py

Data Storage

The application uses a JSON file named "contacts.json" to store contact information.

Example structure:

{
    "1": {
        "name": "Ali",
        "phone": "03001234567"
    },
    "2": {
        "name": "Ahmed",
        "phone": "03111234567"
    }
}

The application loads existing contacts when it starts and saves the updated contact data when the user exits.

Note: The "contacts.json" file is created automatically when the application saves contacts for the first time.

Example Usage

-----Contact-Manager-----
1. Add contact
2. View contacts
3. Delete contact
4. Exit

Enter 1, 2, 3, or 4: 1

Enter name: Ali
Enter phone number for Ali: 03001234567

✓ Contact has been added!

Current Limitations

- Contacts cannot currently be edited.
- Phone numbers are not validated.
- Contacts are saved when the user exits the application.
- The application uses a local JSON file rather than a database.

Future Improvements

- Add an option to update existing contacts.
- Implement phone number validation.
- Add contact searching by name.
- Improve data-saving reliability.
- Introduce a database such as SQLite.
- Organize the application into separate modules as it grows.

Author

Sami Naeem

ICS Physics Student | Exploring Computer Science, Programming, Mathematics & Technology.

---

This project is part of my Python learning journey, focused on strengthening programming fundamentals through practical projects.
