import mysql.connector


class mydb:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            database='library_mgmt',
                                            user='root',
                                            password='password')
        self.my_cursor = self.conn.cursor()

    def executing(self, query, values):
        try:
            self.my_cursor.execute(query, values)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def executing_id(self, query, values):
        try:
            self.my_cursor.execute(query, values)
            self.conn.commit()
            return self.my_cursor.lastrowid
        except Exception as e:
            print(e)
            return False

    def show(self, query):
        self.my_cursor.execute(query)
        return self.my_cursor.fetchall()

    def show_by(self, query, values):
        self.my_cursor.execute(query, values)
        return self.my_cursor.fetchall()

    def cleartable(self, query):
        self.my_cursor.execute(query)
        self.conn.commit()
        return True
