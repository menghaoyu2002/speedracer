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
        self.label['text'] = str(round(float(val), 3))

class UserInterface:
    def __init__(self, root) -> None:
        root.title('Typeracer AutoTyper')
        mainframe = ttk.Frame(root, padding=10)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


        # x label and sliders
        X = ttk.Label(root, text='x value of box position:', font='Verdana', padding=5)
        X.grid(column=0, row=0, sticky='nw')
        x_value = StringVar()
        x_label = ttk.Label(root,text=0.0, font="Verdana", padding=5)
        x_label.grid(column=1, row=0, sticky='nw')
        x_scale = Slider(SCREEN_WITDTH, x_value, x_label)
        x_scale.scale.grid(column=0, row=1, sticky='nw')

        # y labels and sliders
        Y = ttk.Label(root, text='y value of box position:', font='Verdana', padding=5)
        Y.grid(column=0, row=4, sticky='nw')
        y_value = StringVar()
        y_label = ttk.Label(root, text=0.0, font='Verdana', padding=5)
        y_label.grid(column=1, row=4, sticky='nw')
        y_scale = Slider(SCREEN_HEIGHT, y_value, y_label)
        y_scale.scale.grid(column=0, row=5, sticky='nw')

        # height labels and sliders
        height = ttk.Label(root, text='The height of the box:', font='Verdana', padding=5)
        height.grid(column=0, row=6, sticky='nw')
        height_value = StringVar()
        height_label = ttk.Label(root, text=0.0, font='Verdana', padding=5)
        height_label.grid(column=1, row=6, sticky='nw')
        height_scale = Slider(SCREEN_HEIGHT, height_value, height_label)
        height_scale.scale.grid(column=0, row=7, sticky='nw')

        # width labels and sliders
        width = ttk.Label(root, text='The width of the box:', font='Verdana', padding=5)
        width.grid(column=0, row=8, sticky='nw')
        width_value = StringVar()
        width_label = ttk.Label(root, text=0.0, font='Verdana', padding=5)
        width_label.grid(column=1, row=8, sticky='nw')
        width_scale = Slider(SCREEN_HEIGHT, width_value, width_label)
        width_scale.scale.grid(column=0, row=9, sticky='nw')

        # delay label and sliders
        width = ttk.Label(root, text='The typing delay is:', font='Verdana', padding=5)
        width.grid(column=0, row=10, sticky='nw')
        delay_value = StringVar()
        delay_label = ttk.Label(root, text=0.0, font='Verdana', padding=5)
        delay_label.grid(column=1, row=10, sticky='nw')
        delay_scale = Slider(1.0, delay_value, delay_label)
        delay_scale.scale.grid(column=0, row=11, sticky='nw')




UserInterface(root)
root.mainloop()