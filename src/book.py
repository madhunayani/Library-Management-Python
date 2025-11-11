"""
Book class for Library Management System
Represents a book entity with all its attributes and methods
"""

class Book:
    """
    Book class to store book information and manage availability
    
    Attributes:
        title (str): Title of the book
        author (str): Author name
        isbn (str): International Standard Book Number (unique identifier)
        genre (str): Genre/category of the book
        quantity (int): Number of copies available
    """
    
    def __init__(self, title, author, isbn, genre, quantity):
        """
        Initialize a Book object
        
        Args:
            title (str): Title of the book
            author (str): Author name
            isbn (str): ISBN number
            genre (str): Book genre
            quantity (int): Number of copies
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity
    
    def update_quantity(self, new_quantity):
        """
        Update the quantity of books available
        
        Args:
            new_quantity (int): New quantity value
            
        Returns:
            bool: True if updated successfully, False otherwise
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
            return True
        else:
            print("Error: Quantity cannot be negative.")
            return False
    
    def is_available(self):
        """
        Check if the book is available for borrowing
        
        Returns:
            bool: True if quantity > 0, False otherwise
        """
        return self.quantity > 0
    
    def get_title(self):
        """Get book title"""
        return self.title
    
    def get_author(self):
        """Get book author"""
        return self.author
    
    def get_isbn(self):
        """Get book ISBN"""
        return self.isbn
    
    def get_genre(self):
        """Get book genre"""
        return self.genre
    
    def get_quantity(self):
        """Get book quantity"""
        return self.quantity
    
    def update_details(self, title=None, author=None, genre=None):
        """
        Update book details (title, author, or genre)
        
        Args:
            title (str, optional): New title
            author (str, optional): New author
            genre (str, optional): New genre
        """
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
    
    def __str__(self):
        """
        String representation of Book object
        
        Returns:
            str: Formatted book information
        """
        availability = "Available" if self.is_available() else "Not Available"
        return f"[ISBN: {self.isbn}] {self.title} by {self.author} | Genre: {self.genre} | Quantity: {self.quantity} | Status: {availability}"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', '{self.genre}', {self.quantity})"
