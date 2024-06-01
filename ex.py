import random

# Dictionary to store books
library = {
    "001": {"title": "1984", "author": "George Orwell", "year": 1949, "is_borrowed": False}
}

# Set to store borrowed book IDs
borrowed_books = set()

# Function to search by title
def search_title(library):
    title = input("What is the book title? ")
    found_books = [book for book in library.values() if book['title'].lower() == title.lower()]
    if found_books:
        for book in found_books:
            print(f"The book '{book['title']}' by {book['author']} exists in the library.")
    else:
        print("Book does not exist in the library. Try to add it.")

# Function to search by author
def search_author(library):
    author = input("What is the name of the author? ")
    found_books = [book for book in library.values() if book['author'].lower() == author.lower()]
    if found_books:
        for book in found_books:
            print(f"The book '{book['title']}' by {book['author']} exists in the library.")
    else:
        print("Book does not exist in the library. Try to add it.")

# Function to add a book
def add_book(library):
    book_id = input("What is the book ID? ")
    if book_id in library:
        print("Book ID already exists.")
    else:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the year of publication: ")
        library[book_id] = {'title': title, 'author': author, 'year': year, 'is_borrowed': False}
        print("Book added successfully.")

# Function to remove a book
def remove_books(library):
    book_id = input("What is the book ID? ")
    if book_id in library:
        del library[book_id]
        print("The book has been removed from the library.")
    else:
        print("The book is not in the library.")

# Function to list all books
def list_books(library):
    if library:
        for book_id, book in library.items():
            print(f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Borrowed: {book['is_borrowed']}")
    else:
        print("The library is empty.")


def borrow_book(library, borrowed_books):
    book_id = input("Enter the book ID to borrow: ")
    if book_id in library:
        if not library[book_id]['is_borrowed']:
            library[book_id]['is_borrowed'] = True
            borrowed_books.add(book_id)
            print(f"You have borrowed '{library[book_id]['title']}'.")
        else:
            print("The book is already borrowed.")
    else:
        print("The book ID does not exist in the library.")

# Function to mark a book as returned
def return_book(library, borrowed_books):
    book_id = input("Enter the book ID to return: ")
    if book_id in library:
        if library[book_id]['is_borrowed']:
            library[book_id]['is_borrowed'] = False
            borrowed_books.discard(book_id)
            print(f"You have returned '{library[book_id]['title']}'.")
        else:
            print("The book was not borrowed.")
    else:
        print("The book ID does not exist in the library.")



# Main program loop
while True:
    print("\nThe Library System")
    print("Type the number of the option you choose")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book by title")
    print("4. Search by author")
    print("5. List all the books in the library")
    print("6. Exit")
    option_chosen = input()

    if option_chosen == "1":
        add_book(library)
    elif option_chosen == "2":
        remove_books(library)
    elif option_chosen == "3":
        search_title(library)
    elif option_chosen == "4":
        search_author(library)
    elif option_chosen == "5":
        list_books(library)
    elif option_chosen == "6":
        borrow_book(library, borrowed_books)
    elif option_chosen == "7":
        return_book(library, borrowed_books)
    elif option_chosen == "8":
        print("Exiting the library system.")
        break
    else:
        print("Invalid option. Please try again.")
