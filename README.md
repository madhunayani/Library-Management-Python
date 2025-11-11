# Library Management System

A console-based Library Management System built with Python using Object-Oriented Programming (OOP) principles.

## 📖 Overview

This system simulates a real-world library management solution that handles book management, borrower registration, borrowing/returning operations, and comprehensive search functionality. Built as part of the VENHAN Backend Assignment.

## ✨ Features

- **Book Management**: Add, update, remove, and display books with availability tracking
- **Borrower Management**: Register library members and manage their information
- **Borrowing/Returning**: Borrow books with automatic 14-day due date calculation and overdue detection
- **Search Functionality**: Find books by title, author, genre, or ISBN (case-insensitive, partial matching)
- **Reports & Statistics**: View library statistics and overdue books report

## 🛠️ Technical Requirements

- **Python**: 3.8 or higher
- **Libraries**: Standard library only (datetime)
- **OS**: Ubuntu/Linux, Windows, macOS

## 📁 Project Structure

```
library-management-python/
├── src/
│   ├── __init__.py       # Package initializer
│   ├── book.py           # Book class definition
│   ├── borrower.py       # Borrower class definition
│   └── library.py        # Library management class
├── main.py               # Main entry point with menu
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

## 🚀 Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/library-management-python.git
cd library-management-python
```

### 2. Verify Python Installation

```
python3 --version
# Should show Python 3.8 or higher
```

### 3. Run the Application

```
python3 main.py
```

## 📖 Usage Guide

### Main Menu

When you run the application, you'll see an interactive menu:

```
MAIN MENU
1. 📖 Book Management
2. 👥 Borrower Management
3. 🔄 Borrow/Return Books
4. 🔍 Search Books
5. 📊 Reports & Statistics
6. ❌ Exit
```

### Example Workflow

#### 1. Add a Book
Navigate to: `Book Management` → `Add New Book`

```
Enter book title: The Alchemist
Enter author name: Paulo Coelho
Enter ISBN: 978-0062315007
Enter genre: Fiction
Enter quantity: 5
✅ Book 'The Alchemist' added successfully!
```

#### 2. Register a Borrower
Navigate to: `Borrower Management` → `Register New Borrower`

```
Enter borrower name: Rahul Kumar
Enter contact: rahul@email.com
Enter membership ID: MEM001
✅ Borrower 'Rahul Kumar' registered successfully!
```

#### 3. Borrow a Book
Navigate to: `Borrow/Return Books` → `Borrow a Book`

```
Enter membership ID: MEM001
Enter ISBN: 978-0062315007
✅ Book 'The Alchemist' borrowed successfully by Rahul Kumar!
   Borrow Date: 2025-11-12 01:00:00
   Due Date: 2025-11-26 01:00:00
   Please return within 14 days!
```

#### 4. Search for Books
Navigate to: `Search Books` → `Search by Title`

```
Enter title to search: python

🔍 Found 2 book(s) matching title 'python':
1. [ISBN: 978-1593279288] Python Crash Course by Eric Matthes | Genre: Programming | Quantity: 5 | Status: Available
2. [ISBN: 978-1449355739] Learning Python by Mark Lutz | Genre: Programming | Quantity: 2 | Status: Available
```

## 🎓 OOP Concepts Implemented

### 1. Encapsulation
- All class attributes accessed through getter/setter methods
- Data hiding with private implementation details

### 2. Abstraction
- Complex operations hidden behind simple method interfaces
- Users interact with high-level methods

### 3. Modularity
- Separate classes: `Book`, `Borrower`, `Library`
- Each class has single responsibility

### 4. In-Memory Storage
- Lists for storing books and borrowers
- Dictionaries for tracking borrowed books with dates

## 🔑 Key Operations

### Book Class
- Create book with title, author, ISBN, genre, quantity
- Check availability (quantity > 0)
- Update book details and quantity
- Prevent negative quantities

### Borrower Class
- Register with unique membership ID
- Track borrowed books with borrow/due dates
- Update contact information
- View borrowing history

### Library Class
- **CRUD Operations**: Add, update, remove, find books and borrowers
- **Borrowing Logic**: Check availability, calculate due dates, update quantities
- **Returning Logic**: Detect overdue books, restore quantities
- **Search**: Case-insensitive search by title, author, genre, ISBN
- **Reports**: Library statistics, overdue books, available/unavailable books

## ⚠️ Error Handling

The system includes comprehensive error handling:

- ✅ Duplicate ISBN/Membership ID prevention
- ✅ Invalid input validation (empty strings, wrong types)
- ✅ Unavailable book borrowing prevention
- ✅ Non-existent record handling
- ✅ Borrower removal validation (cannot remove if books are borrowed)
- ✅ Keyboard interrupt (Ctrl+C) handling

## 📊 Example Output

### Searching Books by Author
```
Enter author name to search: Coelho

🔍 Found 2 book(s) by author matching 'Coelho':

1. [ISBN: 978-0062315007] The Alchemist by Paulo Coelho | Genre: Fiction | Quantity: 3 | Status: Available
2. [ISBN: 978-0061122415] The Zahir by Paulo Coelho | Genre: Fiction | Quantity: 2 | Status: Available
```

### Overdue Books Report
```
⚠️  OVERDUE BOOKS REPORT
================================================================================

📕 Book: Clean Code (ISBN: 978-0132350884)
   Borrower: Priya Sharma (ID: MEM002)
   Borrow Date: 2025-10-15
   Due Date: 2025-10-29
   Days Overdue: 14 day(s)
   Contact: priya@email.com
================================================================================
```

## 👨‍💻 Author

**[Your Name]**
- GitHub: [@your-username](https://github.com/your-username)
- Email: your.email@example.com

## 🎯 Assignment Details

**Course**: Backend Development  
**Assignment**: Library Management System using Python OOP  
**Institution**: VENHAN  
**Language**: Python 3.8+  
**Focus**: Object-Oriented Programming, CRUD Operations, In-Memory Data Management

## 📝 License

This project is for educational purposes as part of a backend development assignment.

---

**Built with ❤️ using Python**
```

***