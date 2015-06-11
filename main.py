from tkinter  import *

root = Tk()

class MenuOptions:
    def Connection(self):
        print("connected")

class Menus(MenuOptions):
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)



    def topmenu(self):
        m_con = MenuOptions()
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Login", command= m_con.Connection)



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

myapp.mainloop()