import json     # this is python module, use to save & load data
import os       # it is use for system operation & file handling
data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)  # open data in json format
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file) # We open file in write mode & save data in json format

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read the book? (Yes/No): ").lower() == "yes"

    # Create library list
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    
    # now we create condition to add book in the library list
    library.append(new_book)
    save_library(library)
    print(f"The book '{title}' has been added successfully")

# Remove book library
def remove_book(library):
    title = input("Enter the book title to remove it from the library: ")
    init_length = len(library)
    library = [book for book in library if book["title"].lower() != title.lower()]
    
    if len(library) < init_length:
        save_library(library)
        print(f"The book '{title}' has been removed successfully")
    else:
        print(f"The book '{title}' has not been found")

def search_lib(library):
    searchby = input("Search by title or author: ").lower()
    searchterm = input(f"Enter {searchby}: ").lower()

    results = [book for book in library if searchterm in book[searchby].lower()]

    if results:
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("No record found")

# Now make function to display all the books
def display_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("No records found")

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book["read"]])
    percent_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percent_read:.2f}%")

def main():
    library = load_library()

    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_lib(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Thank you!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
