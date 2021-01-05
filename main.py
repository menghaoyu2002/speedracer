from modules.ui import UserInterface
import tkinter as tk

class MainProgram:
    def __init__(self) -> None:
        root = tk.Tk()

        root.resizable(width=False, height=False)
        root.geometry('900x560')
        # constants
        SCREEN_WITDTH = root.winfo_screenwidth()
        SCREEN_HEIGHT = root.winfo_screenheight()

        UserInterface(root, SCREEN_WITDTH, SCREEN_HEIGHT)
        root.mainloop()

run = MainProgram()
