"""
Borrower class for Library Management System
Represents a library member who can borrow books
"""

class Borrower:
    """
    Borrower class to store borrower information and track borrowed books
    
    Attributes:
        name (str): Borrower's full name
        contact (str): Contact information (phone/email)
        membership_id (str): Unique membership identifier
        borrowed_books (list): List of tuples (book, borrow_date, due_date)
    """
    
    def __init__(self, name, contact, membership_id):
        """
        Initialize a Borrower object
        
        Args:
            name (str): Borrower's name
            contact (str): Contact information
            membership_id (str): Unique membership ID
        """
        self.name = name
        self.contact = contact
        self.membership_id = membership_id
        self.borrowed_books = []  # List to track borrowed books with dates
    
    def update_contact(self, new_contact):
        """
        Update borrower's contact information
        
        Args:
            new_contact (str): New contact information
        """
        self.contact = new_contact
        print(f"Contact updated successfully for {self.name}")
    
    def update_name(self, new_name):
        """
        Update borrower's name
        
        Args:
            new_name (str): New name
        """
        self.name = new_name
        print(f"Name updated successfully to {self.name}")
    
    def get_name(self):
        """Get borrower name"""
        return self.name
    
    def get_contact(self):
        """Get borrower contact"""
        return self.contact
    
    def get_membership_id(self):
        """Get membership ID"""
        return self.membership_id
    
    def get_borrowed_books(self):
        """Get list of borrowed books"""
        return self.borrowed_books
    
    def add_borrowed_book(self, book, borrow_date, due_date):
        """
        Add a book to borrower's borrowed books list
        
        Args:
            book (Book): Book object being borrowed
            borrow_date (datetime): Date when book was borrowed
            due_date (datetime): Due date for return
        """
        self.borrowed_books.append({
            'book': book,
            'borrow_date': borrow_date,
            'due_date': due_date
        })
    
    def remove_borrowed_book(self, isbn):
        """
        Remove a book from borrower's borrowed books list (when returned)
        
        Args:
            isbn (str): ISBN of the book being returned
            
        Returns:
            bool: True if removed successfully, False otherwise
        """
        for i, record in enumerate(self.borrowed_books):
            if record['book'].get_isbn() == isbn:
                self.borrowed_books.pop(i)
                return True
        return False
    
    def has_borrowed_books(self):
        """
        Check if borrower has any borrowed books
        
        Returns:
            bool: True if has borrowed books, False otherwise
        """
        return len(self.borrowed_books) > 0
    
    def __str__(self):
        """
        String representation of Borrower object
        
        Returns:
            str: Formatted borrower information
        """
        books_count = len(self.borrowed_books)
        return f"[ID: {self.membership_id}] {self.name} | Contact: {self.contact} | Borrowed Books: {books_count}"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Borrower('{self.name}', '{self.contact}', '{self.membership_id}')"
