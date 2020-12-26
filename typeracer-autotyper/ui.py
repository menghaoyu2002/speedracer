from tkinter import *
from tkinter import ttk


class UserInterface:
    def __init__(self, root) -> None:
        root.title('Typeracer AutoTyper')


root = Tk()
UserInterface(root)
root.update()