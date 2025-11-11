"""
Library Management System - Main Entry Point
Interactive console-based menu system
"""

from src.library import Library
from src.book import Book
from src.borrower import Borrower


def print_header():
    """Print the application header"""
    print("\n" + "=" * 80)
    print("📚 LIBRARY MANAGEMENT SYSTEM")
    print("=" * 80)


def print_main_menu():
    """Display the main menu options"""
    print("\n" + "=" * 80)
    print("MAIN MENU")
    print("=" * 80)
    print("1.  📖 Book Management")
    print("2.  👥 Borrower Management")
    print("3.  🔄 Borrow/Return Books")
    print("4.  🔍 Search Books")
    print("5.  📊 Reports & Statistics")
    print("6.  ❌ Exit")
    print("=" * 80)


def print_book_menu():
    """Display book management submenu"""
    print("\n" + "=" * 80)
    print("📖 BOOK MANAGEMENT")
    print("=" * 80)
    print("1. Add New Book")
    print("2. Update Book Details")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Display Available Books")
    print("6. Display Unavailable Books")
    print("7. Back to Main Menu")
    print("=" * 80)


def print_borrower_menu():
    """Display borrower management submenu"""
    print("\n" + "=" * 80)
    print("👥 BORROWER MANAGEMENT")
    print("=" * 80)
    print("1. Register New Borrower")
    print("2. Update Borrower Details")
    print("3. Remove Borrower")
    print("4. Display All Borrowers")
    print("5. Display Borrower History")
    print("6. Back to Main Menu")
    print("=" * 80)


def print_borrow_return_menu():
    """Display borrow/return submenu"""
    print("\n" + "=" * 80)
    print("🔄 BORROW/RETURN BOOKS")
    print("=" * 80)
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. Check Overdue Books")
    print("4. Back to Main Menu")
    print("=" * 80)


def print_search_menu():
    """Display search submenu"""
    print("\n" + "=" * 80)
    print("🔍 SEARCH BOOKS")
    print("=" * 80)
    print("1. Search by Title")
    print("2. Search by Author")
    print("3. Search by Genre")
    print("4. Search by ISBN")
    print("5. Advanced Search (Multiple Criteria)")
    print("6. Back to Main Menu")
    print("=" * 80)


def print_reports_menu():
    """Display reports submenu"""
    print("\n" + "=" * 80)
    print("📊 REPORTS & STATISTICS")
    print("=" * 80)
    print("1. Library Statistics")
    print("2. Overdue Books Report")
    print("3. Available Books")
    print("4. Unavailable Books")
    print("5. Back to Main Menu")
    print("=" * 80)


def get_valid_input(prompt, input_type=str, allow_empty=False):
    """
    Get validated input from user
    
    Args:
        prompt (str): Input prompt message
        input_type (type): Expected type (str, int, float)
        allow_empty (bool): Allow empty input
        
    Returns:
        Validated input value
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            if not user_input and allow_empty:
                return None
            
            if not user_input:
                print("❌ Input cannot be empty. Please try again.")
                continue
            
            if input_type == int:
                return int(user_input)
            elif input_type == float:
                return float(user_input)
            else:
                return user_input
                
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled by user.")
            return None


def book_management_menu(library):
    """Handle book management operations"""
    while True:
        print_book_menu()
        choice = get_valid_input("\nEnter your choice (1-7): ")
        
        if choice == '1':  # Add New Book
            print("\n--- Add New Book ---")
            title = get_valid_input("Enter book title: ")
            if not title:
                continue
            
            author = get_valid_input("Enter author name: ")
            if not author:
                continue
            
            isbn = get_valid_input("Enter ISBN: ")
            if not isbn:
                continue
            
            genre = get_valid_input("Enter genre: ")
            if not genre:
                continue
            
            quantity = get_valid_input("Enter quantity: ", int)
            if quantity is None:
                continue
            
            book = Book(title, author, isbn, genre, quantity)
            library.add_book(book)
        
        elif choice == '2':  # Update Book
            print("\n--- Update Book Details ---")
            isbn = get_valid_input("Enter ISBN of book to update: ")
            if not isbn:
                continue
            
            book = library.find_book_by_isbn(isbn)
            if not book:
                print(f"❌ Book with ISBN {isbn} not found!")
                continue
            
            print(f"\nCurrent details: {book}")
            print("\nEnter new details (press Enter to skip):")
            
            title = get_valid_input("New title: ", allow_empty=True)
            author = get_valid_input("New author: ", allow_empty=True)
            genre = get_valid_input("New genre: ", allow_empty=True)
            quantity_str = get_valid_input("New quantity: ", allow_empty=True)
            
            quantity = None
            if quantity_str:
                try:
                    quantity = int(quantity_str)
                except ValueError:
                    print("❌ Invalid quantity. Skipping quantity update.")
            
            library.update_book(isbn, title, author, genre, quantity)
        
        elif choice == '3':  # Remove Book
            print("\n--- Remove Book ---")
            isbn = get_valid_input("Enter ISBN of book to remove: ")
            if isbn:
                library.remove_book(isbn)
        
        elif choice == '4':  # Display All Books
            library.display_all_books()
        
        elif choice == '5':  # Display Available Books
            library.display_available_books()
        
        elif choice == '6':  # Display Unavailable Books
            library.display_unavailable_books()
        
        elif choice == '7':  # Back to Main Menu
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-7.")


def borrower_management_menu(library):
    """Handle borrower management operations"""
    while True:
        print_borrower_menu()
        choice = get_valid_input("\nEnter your choice (1-6): ")
        
        if choice == '1':  # Register New Borrower
            print("\n--- Register New Borrower ---")
            name = get_valid_input("Enter borrower name: ")
            if not name:
                continue
            
            contact = get_valid_input("Enter contact (email/phone): ")
            if not contact:
                continue
            
            membership_id = get_valid_input("Enter membership ID: ")
            if not membership_id:
                continue
            
            borrower = Borrower(name, contact, membership_id)
            library.add_borrower(borrower)
        
        elif choice == '2':  # Update Borrower
            print("\n--- Update Borrower Details ---")
            membership_id = get_valid_input("Enter membership ID: ")
            if not membership_id:
                continue
            
            borrower = library.find_borrower_by_id(membership_id)
            if not borrower:
                print(f"❌ Borrower with ID {membership_id} not found!")
                continue
            
            print(f"\nCurrent details: {borrower}")
            print("\nEnter new details (press Enter to skip):")
            
            name = get_valid_input("New name: ", allow_empty=True)
            contact = get_valid_input("New contact: ", allow_empty=True)
            
            library.update_borrower(membership_id, name, contact)
        
        elif choice == '3':  # Remove Borrower
            print("\n--- Remove Borrower ---")
            membership_id = get_valid_input("Enter membership ID: ")
            if membership_id:
                library.remove_borrower(membership_id)
        
        elif choice == '4':  # Display All Borrowers
            library.display_all_borrowers()
        
        elif choice == '5':  # Display Borrower History
            print("\n--- Borrower History ---")
            membership_id = get_valid_input("Enter membership ID: ")
            if membership_id:
                library.display_borrower_history(membership_id)
        
        elif choice == '6':  # Back to Main Menu
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-6.")


def borrow_return_menu(library):
    """Handle borrowing and returning operations"""
    while True:
        print_borrow_return_menu()
        choice = get_valid_input("\nEnter your choice (1-4): ")
        
        if choice == '1':  # Borrow Book
            print("\n--- Borrow a Book ---")
            membership_id = get_valid_input("Enter membership ID: ")
            if not membership_id:
                continue
            
            isbn = get_valid_input("Enter ISBN of book to borrow: ")
            if not isbn:
                continue
            
            library.borrow_book(membership_id, isbn)
        
        elif choice == '2':  # Return Book
            print("\n--- Return a Book ---")
            membership_id = get_valid_input("Enter membership ID: ")
            if not membership_id:
                continue
            
            isbn = get_valid_input("Enter ISBN of book to return: ")
            if not isbn:
                continue
            
            library.return_book(membership_id, isbn)
        
        elif choice == '3':  # Check Overdue Books
            library.check_overdue_books()
        
        elif choice == '4':  # Back to Main Menu
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-4.")


def search_menu(library):
    """Handle search operations"""
    while True:
        print_search_menu()
        choice = get_valid_input("\nEnter your choice (1-6): ")
        
        if choice == '1':  # Search by Title
            query = get_valid_input("\nEnter title to search: ")
            if query:
                library.search_by_title(query)
        
        elif choice == '2':  # Search by Author
            query = get_valid_input("\nEnter author name to search: ")
            if query:
                library.search_by_author(query)
        
        elif choice == '3':  # Search by Genre
            query = get_valid_input("\nEnter genre to search: ")
            if query:
                library.search_by_genre(query)
        
        elif choice == '4':  # Search by ISBN
            query = get_valid_input("\nEnter ISBN to search: ")
            if query:
                library.search_by_isbn(query)
        
        elif choice == '5':  # Advanced Search
            print("\n--- Advanced Search ---")
            print("Enter search criteria (press Enter to skip):")
            title = get_valid_input("Title: ", allow_empty=True)
            author = get_valid_input("Author: ", allow_empty=True)
            genre = get_valid_input("Genre: ", allow_empty=True)
            
            if title or author or genre:
                library.advanced_search(title, author, genre)
            else:
                print("❌ Please provide at least one search criterion.")
        
        elif choice == '6':  # Back to Main Menu
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-6.")


def reports_menu(library):
    """Handle reports and statistics"""
    while True:
        print_reports_menu()
        choice = get_valid_input("\nEnter your choice (1-5): ")
        
        if choice == '1':  # Library Statistics
            library.display_library_stats()
        
        elif choice == '2':  # Overdue Books Report
            library.check_overdue_books()
        
        elif choice == '3':  # Available Books
            library.display_available_books()
        
        elif choice == '4':  # Unavailable Books
            library.display_unavailable_books()
        
        elif choice == '5':  # Back to Main Menu
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-5.")


def main():
    """Main function - Entry point of the application"""
    library = Library()
    
    # Optional: Pre-populate with sample data for testing
    print("💡 Tip: Starting with empty library. Use Book Management to add books.")
    
    print_header()
    print("Welcome to the Library Management System!")
    print("Manage books, borrowers, and track borrowing activities.")
    
    while True:
        print_main_menu()
        choice = get_valid_input("\nEnter your choice (1-6): ")
        
        if choice == '1':  # Book Management
            book_management_menu(library)
        
        elif choice == '2':  # Borrower Management
            borrower_management_menu(library)
        
        elif choice == '3':  # Borrow/Return Books
            borrow_return_menu(library)
        
        elif choice == '4':  # Search Books
            search_menu(library)
        
        elif choice == '5':  # Reports & Statistics
            reports_menu(library)
        
        elif choice == '6':  # Exit
            print("\n" + "=" * 80)
            print("👋 Thank you for using the Library Management System!")
            print("Goodbye!")
            print("=" * 80 + "\n")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user. Exiting...")
        print("👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please report this issue.")
