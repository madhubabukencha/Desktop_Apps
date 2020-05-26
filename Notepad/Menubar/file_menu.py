from tkinter import *
from tkinter import filedialog


class FileMenu:
    """
    A class which contains all File Menu related functions
    """
    def __init__(self, root_obj, text_obj, menu_bar_obj):
        self.root = root_obj
        self.text = text_obj
        self.menu_bar = menu_bar_obj

    def root_file_menu(self):
        """
        Creating a pull down menu and adding it to menu bar
        """
        def file_save():
            """
            Function to save a text as files
            """
            f_save = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            if f_save is None:
                return
            text_to_save = str(self.text.get(0.0, END))
            f_save.write(text_to_save)
            f_save.close()

        file_menu = Menu(self.menu_bar, tearoff=0,
                         background='black',
                         foreground='#D9CB9E',
                         activebackground='#D9CB9E',
                         activeforeground='#374140',
                         activeborderwidth=3)

        file_menu.add_command(label="New", command="")
        file_menu.add_command(label="Open", command="")
        file_menu.add_command(label="Save", command=file_save, accelerator='Ctrl+S')
        file_menu.add_command(label="Save As", command="")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
