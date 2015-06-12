from tkinter  import *
import sys
from hibase import *

root = Tk()
base = Database
base.admin_logon


class MenuOptions:                        ### ALL menu vairables
    def Connection(self):
        print("connected")

    def Test(self):
        print("dupa1")



class UserLogin:
    def main_login(self):
        usr = StringVar()
        paswd = StringVar()

        Label(root, text="User").pack(side=TOP)
        user = Entry(root, textvariable=usr).pack
        user()

        Label(root, text="Password").pack(side=TOP)
        password = Entry(root, textvariable=paswd).pack
        password()
        log_button = Button(root, text=('ENTER'), command=self.auth).pack
        log_button()




class Menus(UserLogin):
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)

    def topmenu(self): #### Rozciagne menu file

        Login = UserLogin()
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Login", command= Login.main_login)  ###### WIDGETS --> Login screen



class App(Frame, Menus):
    def __init__(self, master=None):
        top_menu = Menus()
        top_menu.topmenu()

        Frame.__init__(self, master)
        self.pack()



myapp = App()
myapp.master.title("HiMan")
myapp.master.maxsize(1600, 900)
myapp.master.minsize(600, 400)
myapp.master.wm_iconbitmap("icon.ico")
myapp.mainloop()