from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()

# constants
SCREEN_WITDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()


class Slider:
    def __init__(self, max, variable, label) -> None:
        self.scale = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=0.0, to=max, variable=variable, command=self.update_label)
        self.label = label

    def update_label(self, val):
        self.label['text'] = str(round(float(val), 2))

class UserInterface:
    def __init__(self, root) -> None:
        root.title('Typeracer AutoTyper')
        mainframe = ttk.Frame(root, padding=10)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


        # x label and sliders
        x_value = StringVar()
        x_label = ttk.Label(root)
        x_label.grid(column=0, row=1, sticky='we')
        x_scale = Slider(SCREEN_WITDTH, x_value, x_label)
        x_scale.scale.grid(column=0, row=2, sticky='nw')

        # y labels and sliders
        y_value = StringVar()
        y_label = ttk.Label(root)
        y_label.grid(column=0, row=3, sticky='we')
        y_scale = Slider(SCREEN_HEIGHT, y_value, y_label)
        y_scale.scale.grid(column=0, row=4, sticky='nw')

        # height labels and sliders
        height_value = StringVar()
        height_label = ttk.Label(root)
        height_label.grid(column=0, row=5, sticky='we')
        height_scale = Slider(SCREEN_HEIGHT, height_value, height_label)
        height_scale.scale.grid(column=0, row=6, sticky='nw')

        # delay label and sliders
        delay_value = StringVar()
        delay_label = ttk.Label(root)
        delay_label.grid(column=0, row=7, sticky='we')
        delay_scale = Slider(1.0, delay_value, delay_label)
        delay_scale.scale.grid(column=0, row=8, sticky='nw')




UserInterface(root)
root.mainloop()