from Connector import mydb


class librarian:
    def __init__(self):
        self.exe = mydb()

    def addlibrarian(self, firstname, lastname, email, username, password, contact):
        query = "INSERT INTO librarian (fname, lname, email, username, password, contact) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (firstname, lastname, email, username, password, contact)
        return self.exe.executing(query, values)

    def fetch_librarian(self):
        query = "SELECT username, password FROM librarian"
        return self.exe.show(query)

    def fetch_username(self):
        query = "SELECT username FROM librarian"
        return self.exe.show(query)

    def delete_librarian(self, values):
        query = "DELETE FROM librarian WHERE username=%s"
        values = (values,)
        return self.exe.executing(query, values)


class book:
    def __init__(self):
        self.exe = mydb()

    def add_book(self, name, genre, author):
        query = "INSERT INTO book (book_name, genre, author) VALUES (%s,%s,%s)"
        values = (name, genre, author)
        return self.exe.executing(query, values)

    def update_book(self, name, genre, author, id):
        query = "UPDATE book SET book_name=%s, genre=%s, author=%s WHERE book_id=%s"
        values = (name, genre, author, id)
        return self.exe.executing(query, values)

    def delete_book(self, values):
        query = "DELETE FROM book WHERE book_id=%s"
        values = (values,)
        return self.exe.executing(query, values)

    def fetch_book(self):
        query = "SELECT * FROM book"
        return self.exe.show(query)


class borrower:
    def __init__(self):
        self.exe = mydb()

    def add_borrower(self, fname, lname, contact, email):
        query = "INSERT INTO borrower (fname, lname, contact, email) VALUES (%s,%s,%s,%s)"
        values = (fname, lname, contact, email)
        return self.exe.executing(query, values)

    def update_borrower(self, fname, lname, contact, email, id):
        query = "UPDATE borrower SET fname=%s, lname=%s, contact=%s, email=%s WHERE borrower_id=%s"
        values = (fname, lname, contact, email, id)
        return self.exe.executing(query, values)

    def delete_borrower(self, values):
        query = "DELETE FROM borrower WHERE borrower_id=%s"
        values = (values,)
        return self.exe.executing(query, values)

    def fetch_borrower(self):
        query = "SELECT * FROM borrower"
        return self.exe.show(query)


class issue:
    def __init__(self):
        self.exe = mydb()

    def add_issue(self, bid, bname, brname, contact):
        query = "INSERT INTO book_issue (book_id, book_name, borrower_name, contact) VALUES (%s,%s,%s,%s)"
        values = (bid, bname, brname, contact)
        return self.exe.executing(query, values)

    def update_book_issue(self, id):
        query = "UPDATE book SET availability='No' WHERE book_id=%s"
        values = (id,)
        return self.exe.executing(query, values)

    def return_issue(self, values):
        query = "DELETE FROM book_issue WHERE issue_id=%s"
        values = (values,)
        return self.exe.executing(query, values)

    def update_book_return(self, id):
        query = "UPDATE book SET availability='Yes' WHERE book_id=%s"
        values = (id,)
        return self.exe.executing(query, values)

    def fetch_issue(self):
        query = "SELECT * FROM book_issue"
        return self.exe.show(query)

    def fetch_book(self):
        query = "SELECT book_name FROM book WHERE availability='Yes'"
        return self.exe.show(query)

    def fetch_book_id(self, bname):
        query = "SELECT book_id FROM book WHERE book_name=%s"
        values = (bname,)
        return self.exe.show_by(query, values)
