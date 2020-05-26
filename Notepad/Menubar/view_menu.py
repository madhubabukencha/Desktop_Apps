from tkinter import *
from tkinter.colorchooser import askcolor


class ViewMenu:
    """
    A class which contains all Edit Menu related methods
    """
    def __init__(self, root_obj, text_obj, menu_bar_obj):
        self.root = root_obj
        self.text = text_obj
        self.menu_bar = menu_bar_obj

    def root_view_menu(self):
        """
        Help to set theme and font style
        """
        final_font_type = "DejaVuSansMono"
        font_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 24, 28, 36, 48, 72]
        final_font_size = 8

        def fg_color():
            """
            Function to set font color
            """
            result = askcolor(color="#6A9662",
                              title="Choose Font Color")
            self.text['fg'] = result[1]

        def bg_color():
            """
            Function to set  background color
            """
            result = askcolor(color="#6A9662",
                              title="Choose Background Color")
            self.text['bg'] = result[1]

        def font_size(size):
            """
            Function to set font size
            """
            nonlocal final_font_size
            final_font_size = size
            self.text['font'] = (final_font_type, str(final_font_size))

        def font_type():
            nonlocal final_font_type
            font_top_level = Toplevel(self.root)
            font_top_level.geometry("340x100+230+30")
            font_top_level.title("Font type")

            # Taking font style as input
            font_label = Label(font_top_level, text="Enter Font Style",
                               font=("DejaVuSansMono", 10, "bold"))
            font_label.grid(row=0, column=0, padx=15)
            font_entry = Entry(font_top_level)
            font_entry.grid(row=0, column=1, padx=10, ipadx=30)

            # Taking
            font_top_level.mainloop()

        view_menu = Menu(self.menu_bar, tearoff=0,
                         background="black",
                         foreground="#D9CB9E",
                         activebackground='#D9CB9E',
                         activeforeground='#374140',
                         activeborderwidth=3)
        view_menu.add_command(label="fg color", command=fg_color)
        view_menu.add_command(label="bg color", command=bg_color)

        font_submenu = Menu(view_menu, tearoff=0,
                            background="black",
                            foreground="#D9CB9E",
                            activebackground='#D9CB9E',
                            activeforeground='#374140',
                            activeborderwidth=3)
        # https://stackoverflow.com/questions/27923347/tkinter-menu-command-targets-function-with-arguments
        # https://stackoverflow.com/questions/17677649/tkinter-assign-button-command-in-loop-with-lambda/17677768#17677768
        for size in font_sizes:
            font_submenu.add_command(label=str(size), command=lambda size=size: font_size(size))
        view_menu.add_cascade(label="Font", menu=font_submenu, underline=1)

        view_menu.add_command(label="Font Type", command=font_type)

        self.menu_bar.add_cascade(label="View", menu=view_menu)
