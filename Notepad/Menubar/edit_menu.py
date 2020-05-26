from tkinter import *


class EditMenu:
    """
    A class which contains all Edit Menu related methods
    """
    def __init__(self, root_obj, text_obj, menu_bar_obj):
        self.root = root_obj
        self.text = text_obj
        self.menu_bar = menu_bar_obj

    def root_edit_menu(self):
        """
        Contains the edit menu and edit menu functions
        """
        edit_menu = Menu(self.menu_bar, tearoff=0,
                         background="black",
                         foreground="#D9CB9E",
                         activebackground='#D9CB9E',
                         activeforeground='#374140',
                         activeborderwidth=3)
        edit_menu.add_command(label="Cut", command="")
        edit_menu.add_command(label="Copy", command="")
        edit_menu.add_command(label="Paste", command="")
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete", command="")
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
