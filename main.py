from tkinter  import *
import sqlite3 as lite
from hibase import *


class DatabaseOperation:

    def admin_logon(self):

        try:
            self.con = lite.connect(r"test") ## na potrzeby testu przypisalem baze na sztywno
            self.cur = self.con.cursor()
            self.cur.execute('SELECT name, password FROM users')
            self.data = self.cur.fetchall()
            for row in self.data:
                self.cur.close()
        finally:
            if self.con:
                self.con.close()




class Application(Frame, DatabaseOperation):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.login_widget()

    def login_widget(self):

        self.instruction = Label(self, text = "User:")
        self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

        self.user = Entry(self)
        self.user.grid(row=0, column=1, sticky=W)

        self.instruction = Label(self, text="Password:")
        self.instruction.grid(row=3, column=0, columnspan=2, sticky=W)

        self.password = Entry(self, show="*")
        self.password.grid(row=3, column=1, sticky=W)

        self.submit_button = Button(self, text="Submit", command=self.reveal)
        self.submit_button.grid(row=4, column=1, sticky=W)

        self.text = Text(self, width=35, height=5, wrap=WORD)
        self.text.grid(row=5, column=0, columnspan=2, sticky=W)

    def reveal(self):
        bz = DatabaseOperation()
        bz.admin_logon()
        user = self.user.get()
        password = self.password.get()
        content = (user, password)
        for row in bz.data:
            usr = row[0]
            pswd = row[1]
            data = (usr, pswd)
        if content == (data):
            message = ("Dobre haslo")
        else:
            message = ("dupa")
        self.text.insert(0.0, message)





root = Tk()
root.geometry("800x600")
app = Application(root)
#### Na potrzeby testow


root.mainloop()
