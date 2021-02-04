from tkinter import *
from Menubar.menubar import MenuBar
from tkinter import Scrollbar


if __name__ == "__main__":
    root = Tk()
    root.title("Notepad")
    
    photo_image = PhotoImage(file='valmiki.png')
    root.iconphoto(False, photo_image)

    # geometry("window width x window height + position right + position down")
    root.geometry("900x570+270+30")
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    # http://effbot.org/tkinterbook/text.htm
    text_area = Text(root, bg="azure2",
                     fg="Black",
                     yscrollcommand=scrollbar.set,
                     font=('DejaVuSansMono', '10'))
    text_area.pack(expand=True, fill="both")

    # Menu bar
    my_menu_bar = MenuBar(root, text_area)
    # Above Menubar class contains below sub menus
    my_menu_bar.file_menu_bar()
    my_menu_bar.edit_menu_bar()
    my_menu_bar.view_menu_bar()
    my_menu_bar.display()
    root.mainloop()


# ####Usefull Links######
# Background colors
# https://stackoverflow.com/questions/43372610/changing-background-color-from-text-widget-not-possible
