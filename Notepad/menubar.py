from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from functools import partial

class Menubar:
    """
    This class deals with menubar
    
    Documentation for menubar:
    http://effbot.org/tkinterbook/menu.htm
    """
    def __init__(self, root, text_area):
        self.root = root
        self.text = text_area
        # Creating top level menubar
        self.menubar = Menu(self.root)

    def filemenu(self):
        """
        Creating a pulldown menu and adding it to menu bar
        """
        def file_save():
            f_save = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            if f_save is None:
                return
            text_to_save = str(self.text.get(0.0, END))
            f_save.write(text_to_save)
            f_save.close()
            
        filemenu = Menu(self.menubar, tearoff=0,
                background='black',
                foreground='#D9CB9E',
                activebackground='#D9CB9E',
                activeforeground='#374140',
                activeborderwidth=3)
        filemenu.add_command(label="New", command="")
        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command=file_save, accelerator='Ctrl+S')
        filemenu.add_command(label="Save As", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.destroy)
        self.menubar.add_cascade(label="File", menu=filemenu)

    def editmenu(self):
        """
        Contains the edit menu and edit menu functions
        """
        editmenu = Menu(self.menubar, tearoff=0,
                        background="black",
                        foreground="#D9CB9E",
                        activebackground='#D9CB9E',
                        activeforeground='#374140',
                        activeborderwidth=3)
        editmenu.add_command(label="Cut", command="")
        editmenu.add_command(label="Copy", command="")
        editmenu.add_command(label="Paste", command="")
        editmenu.add_separator()
        editmenu.add_command(label="Delete", command="")
        self.menubar.add_cascade(label="Edit", menu=editmenu)

    def view(self):
        """
        Help to set theam and font style
        """
        font_stype = ""
        font_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 24, 28, 36, 48, 72]
        final_font_size = 8
        
        def fg_color():
            result = askcolor(color="#6A9662",
                              title = "Bernd's Colour Chooser")
            self.text['fg'] = result[1]

        def bg_color():
            result = askcolor(color="#6A9662",
                              title = "Bernd's Colour Chooser")
            self.text['bg'] = result[1]
            
        def font_size(size):
            final_font_size = size
            print(final_font_size)
            
        viewmenu = Menu(self.menubar, tearoff=0,
                        background="black",
                        foreground="#D9CB9E",
                        activebackground='#D9CB9E',
                        activeforeground='#374140',
                        activeborderwidth=3)
        viewmenu.add_command(label="fg color", command=fg_color)
        viewmenu.add_command(label="bg color", command=bg_color)
        
        font_submenu = Menu(viewmenu,tearoff=0,
                        background="black",
                        foreground="#D9CB9E",
                        activebackground='#D9CB9E',
                        activeforeground='#374140',
                        activeborderwidth=3)
        # https://stackoverflow.com/questions/27923347/tkinter-menu-command-targets-function-with-arguments
        # https://stackoverflow.com/questions/17677649/tkinter-assign-button-command-in-loop-with-lambda/17677768#17677768
        for size in font_sizes:
            font_submenu.add_command(label=str(size), command=lambda size=size:font_size(size))
        viewmenu.add_cascade(label="Font", menu=font_submenu, underline=1)
        
        self.menubar.add_cascade(label="View", menu=viewmenu)
    def display(self):
        self.root.config(menu=self.menubar)

