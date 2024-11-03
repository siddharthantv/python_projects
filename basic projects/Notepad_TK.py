import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:

    def __init__(self, width=300, height=300):
        self.root = Tk()  # Create Tkinter root window
        self.width = width  # Default window width
        self.height = height  # Default window height
        self.text_area = Text(self.root)  # Text area for user input
        self.menu_bar = Menu(self.root)  # Menu bar
        self.file_menu = Menu(self.menu_bar, tearoff=0)  # File menu
        self.edit_menu = Menu(self.menu_bar, tearoff=0)  # Edit menu
        self.help_menu = Menu(self.menu_bar, tearoff=0)  # Help menu
        self.scroll_bar = Scrollbar(self.text_area)  # Scrollbar
        self.file = None  # Current file being edited

        self.setup_window()  # Setup window properties
        self.setup_menus()  # Setup menu items

    def setup_window(self):
        self.root.title("Untitled - Notepad")  # Set window title
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        left = (screen_width - self.width) / 2  # Calculate left align
        top = (screen_height - self.height) / 2  # Calculate top align
        self.root.geometry(f"{self.width}x{self.height}+{int(left)}+{int(top)}")  # Set window size and position
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.text_area.grid(sticky=N+E+S+W)  # Grid for text area

    def setup_menus(self):
        file_menu_items = [("New", self.new_file), ("Open", self.open_file), ("Save", self.save_file),
                           ("Exit", self.quit_application)]
        edit_menu_items = [("Cut", self.cut), ("Copy", self.copy), ("Paste", self.paste)]
        help_menu_items = [("About Notepad", self.show_about)]

        for label, command in file_menu_items:
            self.file_menu.add_command(label=label, command=command)

        for label, command in edit_menu_items:
            self.edit_menu.add_command(label=label, command=command)

        for label, command in help_menu_items:
            self.help_menu.add_command(label=label, command=command)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menu_bar)
        self.scroll_bar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)

    def quit_application(self):
        self.root.destroy()

    def show_about(self):
        showinfo("Notepad", "Siddhz")

    def open_file(self):
        filename = askopenfilename(defaultextension=".txt",
                                   filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if filename:
            self.file = filename
            self.root.title(os.path.basename(filename) + " - Notepad")
            with open(filename, "r") as file:
                self.text_area.delete(1.0, END)
                self.text_area.insert(1.0, file.read())

    def new_file(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.text_area.delete(1.0, END)

    def save_file(self):
        if self.file is None:
            self.file = asksaveasfilename(initialfile="Untitled.txt",
                                           defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.file:
                with open(self.file, "w") as file:
                    file.write(self.text_area.get(1.0, END))
                self.root.title(os.path.basename(self.file) + " - Notepad")
        else:
            with open(self.file, "w") as file:
                file.write(self.text_area.get(1.0, END))

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    notepad = Notepad(width=600, height=400)
    notepad.run()
