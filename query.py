from connector import mydb


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
