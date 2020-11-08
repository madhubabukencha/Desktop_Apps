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
            If file is new then it will as for saving(nothing but save as)
            If you just opened a file then it wouldn't say anything. Just saves the content
            """
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
                                              title="Save")
            if f_save is None:
                return
            text_to_save = str(self.text.get(0.0, END))
            f_save.write(text_to_save)
            # window  name after saving file
            self.file_name = f_save.name
            self.root.title(self.file_name)
            f_save.close()

        def open_file():
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
        file_menu.add_command(label="Open", command=open_file)
        file_menu.add_command(label="Save", command=file_save)
        file_menu.add_command(label="Save As", command=file_saveas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
