"""
Library class for Library Management System
Core class that manages books, borrowers, and their operations
"""

class Library:
    """
    Library class to manage books and borrowers with CRUD operations
    
    Attributes:
        books (list): List of Book objects
        borrowers (list): List of Borrower objects
    """
    
    def __init__(self):
        """
        Initialize a Library object with empty lists for books and borrowers
        """
        self.books = []
        self.borrowers = []
    
    # ==================== BOOK MANAGEMENT ====================
    
    def add_book(self, book):
        """
        Add a new book to the library
        
        Args:
            book (Book): Book object to add
            
        Returns:
            bool: True if added successfully, False if ISBN already exists
        """
        # Check if book with same ISBN already exists
        for existing_book in self.books:
            if existing_book.get_isbn() == book.get_isbn():
                print(f"Error: Book with ISBN {book.get_isbn()} already exists!")
                return False
        
        self.books.append(book)
        print(f"✅ Book '{book.get_title()}' added successfully!")
        return True
    
    def remove_book(self, isbn):
        """
        Remove a book from the library by ISBN
        
        Args:
            isbn (str): ISBN of the book to remove
            
        Returns:
            bool: True if removed successfully, False if not found
        """
        for i, book in enumerate(self.books):
            if book.get_isbn() == isbn:
                removed_book = self.books.pop(i)
                print(f"✅ Book '{removed_book.get_title()}' removed successfully!")
                return True
        
        print(f"❌ Error: Book with ISBN {isbn} not found!")
        return False
    
    def update_book(self, isbn, title=None, author=None, genre=None, quantity=None):
        """
        Update book details by ISBN
        
        Args:
            isbn (str): ISBN of the book to update
            title (str, optional): New title
            author (str, optional): New author
            genre (str, optional): New genre
            quantity (int, optional): New quantity
            
        Returns:
            bool: True if updated successfully, False if not found
        """
        for book in self.books:
            if book.get_isbn() == isbn:
                if title:
                    book.update_details(title=title)
                if author:
                    book.update_details(author=author)
                if genre:
                    book.update_details(genre=genre)
                if quantity is not None:
                    book.update_quantity(quantity)
                
                print(f"✅ Book with ISBN {isbn} updated successfully!")
                return True
        
        print(f"❌ Error: Book with ISBN {isbn} not found!")
        return False
    
    def find_book_by_isbn(self, isbn):
        """
        Find a book by ISBN
        
        Args:
            isbn (str): ISBN to search for
            
        Returns:
            Book or None: Book object if found, None otherwise
        """
        for book in self.books:
            if book.get_isbn() == isbn:
                return book
        return None
    
    def display_all_books(self):
        """
        Display all books in the library with their availability status
        """
        if not self.books:
            print("📚 No books in the library yet.")
            return
        
        print("\n" + "=" * 80)
        print("📚 ALL BOOKS IN LIBRARY")
        print("=" * 80)
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print("=" * 80 + "\n")
    
    def get_total_books(self):
        """
        Get total number of unique books (not copies)
        
        Returns:
            int: Number of books
        """
        return len(self.books)
    
    def get_total_copies(self):
        """
        Get total number of book copies in library
        
        Returns:
            int: Total copies
        """
        return sum(book.get_quantity() for book in self.books)
    
    # ==================== BORROWER MANAGEMENT ====================
    
    def add_borrower(self, borrower):
        """
        Add a new borrower to the library
        
        Args:
            borrower (Borrower): Borrower object to add
            
        Returns:
            bool: True if added successfully, False if membership ID already exists
        """
        # Check if borrower with same membership ID already exists
        for existing_borrower in self.borrowers:
            if existing_borrower.get_membership_id() == borrower.get_membership_id():
                print(f"Error: Borrower with ID {borrower.get_membership_id()} already exists!")
                return False
        
        self.borrowers.append(borrower)
        print(f"✅ Borrower '{borrower.get_name()}' registered successfully!")
        return True
    
    def remove_borrower(self, membership_id):
        """
        Remove a borrower from the library by membership ID
        Note: Cannot remove if borrower has borrowed books
        
        Args:
            membership_id (str): Membership ID of borrower to remove
            
        Returns:
            bool: True if removed successfully, False if not found or has borrowed books
        """
        for i, borrower in enumerate(self.borrowers):
            if borrower.get_membership_id() == membership_id:
                # Check if borrower has borrowed books
                if borrower.has_borrowed_books():
                    print(f"❌ Error: Cannot remove borrower '{borrower.get_name()}' - they have unreturned books!")
                    return False
                
                removed_borrower = self.borrowers.pop(i)
                print(f"✅ Borrower '{removed_borrower.get_name()}' removed successfully!")
                return True
        
        print(f"❌ Error: Borrower with ID {membership_id} not found!")
        return False
    
    def update_borrower(self, membership_id, name=None, contact=None):
        """
        Update borrower details by membership ID
        
        Args:
            membership_id (str): Membership ID of borrower to update
            name (str, optional): New name
            contact (str, optional): New contact
            
        Returns:
            bool: True if updated successfully, False if not found
        """
        for borrower in self.borrowers:
            if borrower.get_membership_id() == membership_id:
                if name:
                    borrower.update_name(name)
                if contact:
                    borrower.update_contact(contact)
                
                print(f"✅ Borrower with ID {membership_id} updated successfully!")
                return True
        
        print(f"❌ Error: Borrower with ID {membership_id} not found!")
        return False
    
    def find_borrower_by_id(self, membership_id):
        """
        Find a borrower by membership ID
        
        Args:
            membership_id (str): Membership ID to search for
            
        Returns:
            Borrower or None: Borrower object if found, None otherwise
        """
        for borrower in self.borrowers:
            if borrower.get_membership_id() == membership_id:
                return borrower
        return None
    
    def display_all_borrowers(self):
        """
        Display all registered borrowers
        """
        if not self.borrowers:
            print("👥 No borrowers registered yet.")
            return
        
        print("\n" + "=" * 80)
        print("👥 ALL REGISTERED BORROWERS")
        print("=" * 80)
        for i, borrower in enumerate(self.borrowers, 1):
            print(f"{i}. {borrower}")
        print("=" * 80 + "\n")
    
    def get_total_borrowers(self):
        """
        Get total number of registered borrowers
        
        Returns:
            int: Number of borrowers
        """
        return len(self.borrowers)
    
    # ==================== BORROWING & RETURNING ====================
    
    def borrow_book(self, membership_id, isbn):
        """
        Process book borrowing with due date calculation (14 days)
        
        Args:
            membership_id (str): Membership ID of borrower
            isbn (str): ISBN of book to borrow
            
        Returns:
            bool: True if borrowed successfully, False otherwise
        """
        from datetime import datetime, timedelta
        
        # Find borrower
        borrower = self.find_borrower_by_id(membership_id)
        if not borrower:
            print(f"❌ Error: Borrower with ID {membership_id} not found!")
            return False
        
        # Find book
        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"❌ Error: Book with ISBN {isbn} not found!")
            return False
        
        # Check availability
        if not book.is_available():
            print(f"❌ Error: Book '{book.get_title()}' is currently unavailable!")
            return False
        
        # Process borrowing
        book.update_quantity(book.get_quantity() - 1)
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=14)  # 14 days borrowing period
        
        # Add to borrower's borrowed books list
        borrower.add_borrowed_book(book, borrow_date, due_date)
        
        print(f"✅ Book '{book.get_title()}' borrowed successfully by {borrower.get_name()}!")
        print(f"   Borrow Date: {borrow_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Due Date: {due_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Please return within 14 days!")
        
        return True
    
    def return_book(self, membership_id, isbn):
        """
        Process book return
        
        Args:
            membership_id (str): Membership ID of borrower
            isbn (str): ISBN of book to return
            
        Returns:
            bool: True if returned successfully, False otherwise
        """
        from datetime import datetime
        
        # Find borrower
        borrower = self.find_borrower_by_id(membership_id)
        if not borrower:
            print(f"❌ Error: Borrower with ID {membership_id} not found!")
            return False
        
        # Find book
        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"❌ Error: Book with ISBN {isbn} not found!")
            return False
        
        # Check if borrower actually borrowed this book
        borrowed_books = borrower.get_borrowed_books()
        book_found = False
        
        for record in borrowed_books:
            if record['book'].get_isbn() == isbn:
                book_found = True
                due_date = record['due_date']
                
                # Check if overdue
                current_date = datetime.now()
                if current_date > due_date:
                    days_overdue = (current_date - due_date).days
                    print(f"⚠️  Warning: Book is {days_overdue} day(s) overdue!")
                
                break
        
        if not book_found:
            print(f"❌ Error: Borrower {borrower.get_name()} has not borrowed this book!")
            return False
        
        # Process return
        book.update_quantity(book.get_quantity() + 1)
        borrower.remove_borrowed_book(isbn)
        
        print(f"✅ Book '{book.get_title()}' returned successfully by {borrower.get_name()}!")
        print(f"   Return Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return True
    
    def check_overdue_books(self):
        """
        Check and display all overdue books across all borrowers
        """
        from datetime import datetime
        
        current_date = datetime.now()
        overdue_found = False
        
        print("\n" + "=" * 80)
        print("⚠️  OVERDUE BOOKS REPORT")
        print("=" * 80)
        
        for borrower in self.borrowers:
            borrowed_books = borrower.get_borrowed_books()
            
            for record in borrowed_books:
                due_date = record['due_date']
                
                if current_date > due_date:
                    overdue_found = True
                    days_overdue = (current_date - due_date).days
                    book = record['book']
                    borrow_date = record['borrow_date']
                    
                    print(f"\n📕 Book: {book.get_title()} (ISBN: {book.get_isbn()})")
                    print(f"   Borrower: {borrower.get_name()} (ID: {borrower.get_membership_id()})")
                    print(f"   Borrow Date: {borrow_date.strftime('%Y-%m-%d')}")
                    print(f"   Due Date: {due_date.strftime('%Y-%m-%d')}")
                    print(f"   Days Overdue: {days_overdue} day(s)")
                    print(f"   Contact: {borrower.get_contact()}")
        
        if not overdue_found:
            print("\n✅ No overdue books! All borrowers are on time.")
        
        print("=" * 80 + "\n")
    
    def display_borrower_history(self, membership_id):
        """
        Display borrowing history for a specific borrower
        
        Args:
            membership_id (str): Membership ID of borrower
        """
        from datetime import datetime
        
        borrower = self.find_borrower_by_id(membership_id)
        if not borrower:
            print(f"❌ Error: Borrower with ID {membership_id} not found!")
            return
        
        borrowed_books = borrower.get_borrowed_books()
        
        print("\n" + "=" * 80)
        print(f"📖 BORROWING HISTORY - {borrower.get_name()} (ID: {membership_id})")
        print("=" * 80)
        
        if not borrowed_books:
            print("No books currently borrowed.")
        else:
            current_date = datetime.now()
            
            for i, record in enumerate(borrowed_books, 1):
                book = record['book']
                borrow_date = record['borrow_date']
                due_date = record['due_date']
                
                status = "✅ On Time"
                if current_date > due_date:
                    days_overdue = (current_date - due_date).days
                    status = f"⚠️  OVERDUE by {days_overdue} day(s)"
                
                print(f"\n{i}. {book.get_title()} by {book.get_author()}")
                print(f"   ISBN: {book.get_isbn()}")
                print(f"   Borrowed: {borrow_date.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"   Due: {due_date.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"   Status: {status}")
        
        print("=" * 80 + "\n")
    
    def get_available_books(self):
        """
        Get list of all available books (quantity > 0)
        
        Returns:
            list: List of available Book objects
        """
        return [book for book in self.books if book.is_available()]
    
    def get_unavailable_books(self):
        """
        Get list of all unavailable books (quantity = 0)
        
        Returns:
            list: List of unavailable Book objects
        """
        return [book for book in self.books if not book.is_available()]
    
    # ==================== SEARCH FUNCTIONALITY ====================
    
    def search_by_title(self, title):
        """
        Search for books by title (case-insensitive, partial match)
        
        Args:
            title (str): Title or partial title to search for
            
        Returns:
            list: List of matching Book objects
        """
        search_term = title.lower()
        results = [book for book in self.books if search_term in book.get_title().lower()]
        
        if results:
            print(f"\n🔍 Found {len(results)} book(s) matching title '{title}':\n")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book}")
        else:
            print(f"\n❌ No books found with title containing '{title}'")
        
        return results
    
    def search_by_author(self, author):
        """
        Search for books by author (case-insensitive, partial match)
        
        Args:
            author (str): Author name or partial name to search for
            
        Returns:
            list: List of matching Book objects
        """
        search_term = author.lower()
        results = [book for book in self.books if search_term in book.get_author().lower()]
        
        if results:
            print(f"\n🔍 Found {len(results)} book(s) by author matching '{author}':\n")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book}")
        else:
            print(f"\n❌ No books found by author matching '{author}'")
        
        return results
    
    def search_by_genre(self, genre):
        """
        Search for books by genre (case-insensitive, partial match)
        
        Args:
            genre (str): Genre or partial genre to search for
            
        Returns:
            list: List of matching Book objects
        """
        search_term = genre.lower()
        results = [book for book in self.books if search_term in book.get_genre().lower()]
        
        if results:
            print(f"\n🔍 Found {len(results)} book(s) in genre matching '{genre}':\n")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book}")
        else:
            print(f"\n❌ No books found in genre matching '{genre}'")
        
        return results
    
    def search_by_isbn(self, isbn):
        """
        Search for a specific book by exact ISBN match
        
        Args:
            isbn (str): ISBN to search for
            
        Returns:
            Book or None: Book object if found, None otherwise
        """
        book = self.find_book_by_isbn(isbn)
        
        if book:
            print(f"\n🔍 Book found:\n")
            print(f"1. {book}")
        else:
            print(f"\n❌ No book found with ISBN '{isbn}'")
        
        return book
    
    def advanced_search(self, title=None, author=None, genre=None):
        """
        Advanced search combining multiple criteria (AND logic)
        
        Args:
            title (str, optional): Title to search for
            author (str, optional): Author to search for
            genre (str, optional): Genre to search for
            
        Returns:
            list: List of books matching ALL provided criteria
        """
        results = self.books
        
        # Filter by title if provided
        if title:
            title_term = title.lower()
            results = [book for book in results if title_term in book.get_title().lower()]
        
        # Filter by author if provided
        if author:
            author_term = author.lower()
            results = [book for book in results if author_term in book.get_author().lower()]
        
        # Filter by genre if provided
        if genre:
            genre_term = genre.lower()
            results = [book for book in results if genre_term in book.get_genre().lower()]
        
        if results:
            criteria = []
            if title:
                criteria.append(f"title='{title}'")
            if author:
                criteria.append(f"author='{author}'")
            if genre:
                criteria.append(f"genre='{genre}'")
            
            criteria_str = ", ".join(criteria)
            print(f"\n🔍 Found {len(results)} book(s) matching criteria ({criteria_str}):\n")
            
            for i, book in enumerate(results, 1):
                print(f"{i}. {book}")
        else:
            print(f"\n❌ No books found matching the search criteria")
        
        return results
    
    def display_available_books(self):
        """
        Display all books that are currently available for borrowing
        """
        available = self.get_available_books()
        
        if not available:
            print("\n📚 No books currently available for borrowing.")
            return
        
        print("\n" + "=" * 80)
        print("📗 AVAILABLE BOOKS FOR BORROWING")
        print("=" * 80)
        for i, book in enumerate(available, 1):
            print(f"{i}. {book}")
        print("=" * 80 + "\n")
    
    def display_unavailable_books(self):
        """
        Display all books that are currently unavailable (all copies borrowed)
        """
        unavailable = self.get_unavailable_books()
        
        if not unavailable:
            print("\n✅ All books have available copies!")
            return
        
        print("\n" + "=" * 80)
        print("📕 UNAVAILABLE BOOKS (All copies borrowed)")
        print("=" * 80)
        for i, book in enumerate(unavailable, 1):
            print(f"{i}. {book}")
        print("=" * 80 + "\n")
    
    def search_with_availability(self, search_type, query):
        """
        Search with availability status highlighted
        
        Args:
            search_type (str): Type of search ('title', 'author', 'genre')
            query (str): Search query
        """
        if search_type == 'title':
            results = self.search_by_title(query)
        elif search_type == 'author':
            results = self.search_by_author(query)
        elif search_type == 'genre':
            results = self.search_by_genre(query)
        else:
            print("❌ Invalid search type. Use 'title', 'author', or 'genre'")
            return []
        
        if results:
            print("\n📊 Availability Summary:")
            available_count = sum(1 for book in results if book.is_available())
            print(f"   Available: {available_count}/{len(results)}")
            print(f"   Unavailable: {len(results) - available_count}/{len(results)}")
        
        return results
    
    # ==================== LIBRARY STATISTICS ====================
    
    def display_library_stats(self):
        """
        Display overall library statistics
        """
        print("\n" + "=" * 60)
        print("📊 LIBRARY STATISTICS")
        print("=" * 60)
        print(f"Total Books (Unique): {self.get_total_books()}")
        print(f"Total Copies: {self.get_total_copies()}")
        print(f"Total Registered Borrowers: {self.get_total_borrowers()}")
        print("=" * 60 + "\n")
