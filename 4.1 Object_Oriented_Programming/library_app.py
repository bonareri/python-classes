# ==========================================
# LIBRARY MANAGEMENT SYSTEM WITH CLI (OOP)
# ==========================================

# -------- Book Class --------
class Book:
    
    def __init__(self, title, author, book_no):
        self.title = title
        self.author = author
        self.book_no = book_no
        self.is_borrowed = False
        
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"\n'{self.title}' has been borrowed.")
        else:
            print("\nBook is already borrowed.")
            
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"\n'{self.title}' has been returned.")
        else:
            print("\nBook was not borrowed.")
            
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book No: {self.book_no} | {self.title} by {self.author} | Status: {status}"


# -------- Member Class --------
class Member:
    
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print("\nThis book is already borrowed.")
            
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("\nYou did not borrow this book.")
            
    def __str__(self):
        return f"Member ID: {self.member_id} | Name: {self.name} | Borrowed Books: {len(self.borrowed_books)}"


# -------- Library Class --------
class Library:
    
    def __init__(self):
        self.books = []
        self.members = []
        
    def add_book(self, title, author, book_no):
        # prevent duplicate book numbers
        if self.find_book(book_no):
            print("\nBook number already exists.")
            return
        book = Book(title, author, book_no)
        self.books.append(book)
        print("\nBook added successfully.")
        
    def register_member(self, name, member_id):
        if self.find_member(member_id):
            print("\nMember ID already exists.")
            return
        member = Member(name, member_id)
        self.members.append(member)
        print("\nMember registered successfully.")
        
    def find_book(self, book_no):
        for book in self.books:
            if book.book_no == book_no:
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def display_books(self):
        if not self.books:
            print("\nNo books available.")
        for book in self.books:
            print(book)
            
    def display_members(self):
        if not self.members:
            print("\nNo members registered.")
        for member in self.members:
            print(member)


# ==========================================
# CLI MENU SYSTEM
# ==========================================

library = Library()

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. View All Members")
    print("7. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        book_no = int(input("Enter book number: "))
        library.add_book(title, author, book_no)
        
    elif choice == "2":
        name = input("Enter member name: ")
        member_id = int(input("Enter member ID: "))
        library.register_member(name, member_id)
        
    elif choice == "3":
        member_id = int(input("Enter member ID: "))
        book_no = int(input("Enter book number: "))
        member = library.find_member(member_id)
        book = library.find_book(book_no)
        
        if member and book:
            member.borrow_book(book)
        else:
            print("\nInvalid member ID or book number.")
            
    elif choice == "4":
        member_id = int(input("Enter member ID: "))
        book_no = int(input("Enter book number: "))
        member = library.find_member(member_id)
        book = library.find_book(book_no)
        
        if member and book:
            member.return_book(book)
        else:
            print("\nInvalid member ID or book number.")
            
    elif choice == "5":
        library.display_books()
        
    elif choice == "6":
        library.display_members()
        
    elif choice == "7":
        print("\nExiting system. Goodbye!")
        break
        
    else:
        print("\nInvalid choice. Try again.")