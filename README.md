# Library-Management
Library Management System 
A simple command-line Library Management System written in Python. It allows users to add, issue, return, remove, display, search, and count books.

FEATURES
•	Add books with ID, name, author, and number of copies
•	Issue and return books
•	Remove books from the system
•	Display all books in sorted order (by Book ID)
•	Search books by title or author
•	Count total copies in the library

REQUIREMENTS
•	Python 3.8 or above
•	Works on Windows, Mac, and Linux
•	No external libraries required

SETUP & RUN INSTRUCTIONS
1.	Download or clone the project
2.	Run the program using:
python main.py

HOW THE CODE WORKS
The program stores books in a dictionary named books.
Example structure:
books = {"101": {"name": "Python", "author": "Guido", "copies": 3},}
FUNCTIONALITY EXPLAINED
Add Book
Prompts for Book ID, name, author, and copies.
If the ID exists, copies increase.
Issue Book
Reduces copies by one if available.
Return Book
Increases the number of copies.
Remove Book
Deletes a book completely.
Display Books
Lists all books sorted by Book ID.
Search Book
Search by book name or author.
Count Books
Displays total number of copies stored.

MENU FLOW
1. Add Book
2. Issue Book
3. Return Book
4. Remove Book
5. Display Books
6. Search Book
7. Count Books
8. Exit
SAMPLE OUTPUT
LIBRARY MENU
Enter your choice: 1
Enter Book ID: 100
Enter Book Name: Python Basics
Enter Author Name: Alex
Enter number of copies: 5
Book added!

Contributions are welcome! Please open an issue or submit a pull request.
Created by Ravi Bhushan Rai - feel free to reach out at ravibhushanrai3107@gmail.com
Thank you...
