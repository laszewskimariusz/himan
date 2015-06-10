import sqlite3 as lite


class Database:
    file_name = input("Enter Database Name:")


##### CREATING DATABASE
    def creating_data_base(self):
        if self.file_name is self.file_name:
            print("file exist")
        else:
            open(self.file_name, 'w+')

#### CRATING TABLE
    def creating_table(self):
        try:
            con = lite.connect(self.file_name)
            cur = con.cursor()
            cur.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

        finally:
            if con:
                con.close()

#### INSTERT DATA INTO TABLE
    def insert_data(self):
        try:
            con = lite.connect(self.file_name)
            cur = con.cursor()
            cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
            con.commit()

        finally:
            if con:
                con.close()

#### QUERY FROM DATABASE

    def database_query(self):
        try:
            con = lite.connect(self.file_name)
            cur = con.cursor()
            cur.execute('SELECT * FROM stocks')
            print (cur.fetchone())


        finally:
            if con:
                con.close()


class Operation(Database):
#
#  Memo: Create ERR class
#
    def start(self):
        print("WELCOME IN HIMAN\n CHOSE OPTIONS \n 1.CREATE DATABASE\n 2.CREATE TABLE\n 3.ADD DATA TO TABLE\n 4.QUERY DATA\n\n\n")
        choice = ""
        base = Database()

        while choice != "exit":
            choice = input("Chose number : ")
            if choice == '1':
                try:
                    base.creating_data_base()
                except:
                    print("ERROR003")

            elif choice == '2':
                try:
                    base.creating_table()
                except:
                    print("ERROR003")
            elif choice == '3':
                try:
                    base.insert_data()
                except:
                    print("ERROR003")
            if choice == '4':
                try:
                    base.database_query()
                except:
                    print("ERROR003")

            else:
                quit()



#run = Operation()
#run.start()
run = CratingTable()
run.inputdata()