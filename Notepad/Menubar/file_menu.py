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
        self.file_name = ""
        self.file_type = [('Python Files', '*.py'),
                          ('Text Document', '*.txt')]

    def root_file_menu(self):
        """
        Creating a pull down menu and adding it to menu bar
        """
        def file_save():
            """
            If file is new then it will ask for saving(act as 'save as' function)
            If you just opened a file then it wouldn't say anything. It just saves the content
            """
            # File name will set open_file() function
            if self.file_name:
                text_area_text = self.text.get('1.0', 'end-1c')
                save_text = open(self.file_name, 'w')
                save_text.write(text_area_text)
                save_text.close()
            else:
                f_save = filedialog.asksaveasfile(mode="w", filetypes=self.file_type,
                                                  defaultextension=".txt",
                                                  title="Save")
                if f_save is None:
                    return
                text_to_save = str(self.text.get(0.0, END))
                f_save.write(text_to_save)
                # window  name after saving file
                self.file_name = f_save.name
                self.root.title(self.file_name)
                f_save.close()

        def file_saveas():
            """
            Function to save  a text into a new files(Save as)
            """
            f_save = filedialog.asksaveasfile(mode="w", filetypes=self.file_type,
                                              defaultextension=".txt",
                                              title="Save As")
            if f_save is None:
                return
            text_to_save = str(self.text.get(0.0, END))
            f_save.write(text_to_save)
            # window  name after saving file
            self.file_name = f_save.name
            self.root.title(self.file_name)
            f_save.close()

        def open_file():
            """
            Function to open a file
            """
            o_file = filedialog.askopenfile(mode='r', filetypes=self.file_type)
            if o_file is not None:
                self.file_name = o_file.name
                self.root.title(self.file_name)
                content = o_file.read()
                # Deleting content which already present in our text widget
                self.text.delete("1.0", END)
                self.text.insert(END, content)
                o_file.close()

        file_menu = Menu(self.menu_bar, tearoff=0,
                         background='black',
                         foreground='#D9CB9E',
                         activebackground='#D9CB9E',
                         activeforeground='#374140',
                         activeborderwidth=3)

        file_menu.add_command(label="New", command="")
        file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=file_save, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=file_saveas, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy, accelerator="Ctrl+Q")
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        # you can say key bord short cuts to do work
        self.root.bind('<Control-o>', lambda event: open_file())
        self.root.bind('<Control-s>', lambda event: file_save())
        self.root.bind('<Control-S>', lambda event: file_saveas())
