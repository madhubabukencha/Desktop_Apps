from tkinter import *
from tkinter.colorchooser import askcolor
# Remember if you keep . to import a package you might get relative path related error
from Menubar import file_menu
from Menubar import edit_menu
from Menubar import view_menu


class MenuBar:
    """
    This class deals with menu bar
    
    Documentation for menu bar:
    http://effbot.org/tkinterbook/menu.htm
    """
    def __init__(self, root, text_area):
        self.root = root
        self.text = text_area
        # Creating top level menu bar
        self.menu_bar = Menu(self.root)

    def file_menu_bar(self):
        """
        Contains the file menu related functions
        """
        file_menu_obj = file_menu.FileMenu(self.root, self.text, self.menu_bar)
        file_menu_obj.root_file_menu()

    def edit_menu_bar(self):
        """
        Contains the edit menu and edit menu functions
        """
        edit_menu_obj = edit_menu.EditMenu(self.root, self.text, self.menu_bar)
        edit_menu_obj.root_edit_menu()

    def view_menu_bar(self):
        """
        Helps to set theme and font style
        """
        view_menu_obj = view_menu.ViewMenu(self.root, self.text, self.menu_bar)
        view_menu_obj.root_view_menu()

    def display(self):
        self.root.config(menu=self.menu_bar)

