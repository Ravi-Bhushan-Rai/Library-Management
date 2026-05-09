books = {}

def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter number of copies: "))

    if book_id in books:
        books[book_id]["copies"] += copies
        print("Copies added to existing book!")
    else:
        books[book_id] = {
            "name": name,
            "author": author,
            "copies": copies
        }
        print("Book added!")


def issue_book():
    book_id = input("Enter Book ID to Issue: ")
    if book_id in books and books[book_id]["copies"] > 0:
        books[book_id]["copies"] -= 1
        print("Book issued successfully!")
    else:
        print("Book not available!")


def return_book():
    book_id = input("Enter Book ID to return: ")
    if book_id in books:
        books[book_id]["copies"] += 1
        print("Book returned successfully!")
    else:
        print("Invalid Book ID!")


def remove_book():
    book_id = input("Enter Book ID to remove: ")
    if book_id in books:
        del books[book_id]
        print("Book removed!")
    else:
        print("Book not found!")


def display_books():
    if len(books) == 0:
        print("No books in library")
    else:
        print("\nID    Book Name        Author          Copies")

        # SORTING BY BOOK ID (main part)
        for book_id in sorted(books):
            details = books[book_id]
            print(f"{book_id}   {details['name']}   {details['author']}   {details['copies']}")


def search_book():
    keyword = input("Enter book name or author: ").lower()
    found = False

    for book_id, details in books.items():
        if keyword in details["name"].lower() or keyword in details["author"].lower():
            print(f"{book_id}  {details['name']}  {details['author']}  Copies: {details['copies']}")
            found = True

    if not found:
        print("No book found!")


def count_books():
    total = 0
    for details in books.values():
        total += details["copies"]

    print("Total books in library:", total)


while True:
    print("\nLIBRARY MENU")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Remove Book")
    print("5. Display Books")
    print("6. Search Book")
    print("7. Count Books")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        issue_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        remove_book()
    elif choice == 5:
        display_books()
    elif choice == 6:
        search_book()
    elif choice == 7:
        count_books()
    elif choice == 8:
        print("Thank you for using Library System!")
        break
    else:
        print("Invalid Choice!")