from tkinter import *
from menubar import Menubar
from tkinter import Scrollbar



if __name__ == "__main__":
    root = Tk()
    root.title("Notepad")
    # geometry("window width x window height + position right + position down")
    root.geometry("900x570+270+30")
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    # http://effbot.org/tkinterbook/text.htm
    text_area = Text(root, bg="azure2", fg="Black", yscrollcommand = scrollbar.set)
    text_area.pack(expand=True, fill="both")

    # Menu bar
    my_menubar = Menubar(root, text_area)
    my_menubar.filemenu()
    my_menubar.editmenu()
    my_menubar.view()
    my_menubar.display()
    root.mainloop()

# ####Usefull Links######

# Background colors
# https://stackoverflow.com/questions/43372610/changing-background-color-from-text-widget-not-possible
