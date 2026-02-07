# Library Management System

library = []

def add_book():
    book_name = input("Enter book name: ")
    library.append(book_name)
    print("Book added successfully!\n")

def display_books():
    if not library:
        print("No books available in the library.\n")
    else:
        print("Books available in the library:")
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book}")
        print()

def issue_book():
    book_name = input("Enter book name to issue: ")
    if book_name in library:
        library.remove(book_name)
        print("Book issued successfully!\n")
    else:
        print("Book not found!\n")

def return_book():
    book_name = input("Enter book name to return: ")
    library.append(book_name)
    print("Book returned successfully!\n")

while True:
    print("----- Library Management System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        print("Thank you! Exiting Library System.")
        break
    else:
        print("Invalid choice! Please try again.\n")
