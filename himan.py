import sqlite3 as lite


class Database:
    file_name = input("Enter Database Name:")




    def creating_data_base(self):
        if self.file_name is self.file_name:
            print("file exist")
        else:
            open(self.file_name, 'w+')

    def creating_table(self):
        try:
            con = lite.connect(self.file_name)
            cur = con.cursor()
            cur.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

        finally:
            if con:
                con.close()

    def insert_data(self):
        try:
            con = lite.connect(self.file_name)
            cur = con.cursor()
            cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
            con.commit()

        finally:
            if con:
                con.close()





    def database_query(self):
        try:
            con = lite.connect(self.file_name)
            cur = con.cursor()
            cur.execute('SELECT * FROM stocks')
            print (cur.fetchone())


        finally:
            if con:
                con.close()






file1 = Database()

file1.insert_data()
file1.database_query()