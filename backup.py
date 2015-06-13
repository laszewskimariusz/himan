import sqlite3 as lite
import tkinter as tk
from tkinter import ttk



LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Vernada", 9)

class DatabaseOperation:

    def admin_logon(self):

        try:
            self.con = lite.connect(r"test")
            self.cur = self.con.cursor()
            self.cur.execute('SELECT name, password FROM users')
            self.data = self.cur.fetchall()
            for row in self.data:
                self.cur.close()
        finally:
            if self.con:
                self.con.close()





class Himan(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "HiMan")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame, DatabaseOperation):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label = tk.Label(self, text="User:", font=SMALL_FONT)
        label.pack(pady=10,padx=10)


        user = ttk.Entry(self, width='15')
        user.pack()


        label = tk.Label(self, text="Password:", font=SMALL_FONT)
        label.pack(pady=10,padx=10)

        password = ttk.Entry(self, width='15')
        password.pack()

        button = ttk.Button(self, text="Enter", command=self.reveal)
        button.pack(pady=10,padx=100)

        button2 = ttk.Button(self, text="EXIT",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=10,padx=100)



    def reveal(self):
        bz = DatabaseOperation()
        bz.admin_logon()

        content = (user, password)
        for row in bz.data:
            usr = row[0]
            pswd = row[1]
            data = (usr, pswd)
        if content == (data):
            print("OK")










class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()



app = Himan()
app.mainloop()