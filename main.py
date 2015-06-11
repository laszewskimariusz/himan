from tkinter import *

Root = Tk()



class Window():
    def main(self):

        RTitle = Root.title("HIMAN")
        Root.geometry("800x600")
        Root.wm_iconbitmap("icon.ico")
        Root.mainloop()




win = Window()
win.main()
