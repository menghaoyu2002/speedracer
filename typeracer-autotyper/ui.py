from tkinter import *
from tkinter import ttk

root = Tk()

# constants
SCREEN_WITDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()


class Slider:
    def __init__(self, max, variable) -> None:
        self.scale = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=0.0, to=max, variable=variable)

class Field:
    def __init__(self, variable) -> None:
        self.entry = ttk.Entry(root, textvariable=variable, width=7, font="Verdana")

class Preview:
    def __init__(self) -> None:
        pass

class UserInterface:
    def __init__(self, root) -> None:
        root.title('Typeracer AutoTyper')
        mainframe = ttk.Frame(root, padding=10)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # x label
        X = ttk.Label(root, text='x value of box position:', font='Verdana', padding=5)
        X.grid(column=0, row=0, sticky='nw')

        # x variable
        x_value = StringVar()

        # x slider
        x_scale = Slider(SCREEN_WITDTH, x_value)
        x_scale.scale.grid(column=0, row=1, sticky='nw', pady=10, padx=5)

        # x entry field
        x_field = Field(x_value)
        x_field.entry.grid(column=1, row=1)

        # y labels
        Y = ttk.Label(root, text='y value of box position:', font='Verdana', padding=5)
        Y.grid(column=0, row=4, sticky='nw')

        # y variable
        y_value = StringVar()

        # y sliders
        y_scale = Slider(SCREEN_HEIGHT, y_value)
        y_scale.scale.grid(column=0, row=5, sticky='nw', pady=10, padx=5)

        # y entry field
        y_field = Field(y_value)
        y_field.entry.grid(column=1, row=5)

        # height labels
        height = ttk.Label(root, text='The height of the box:', font='Verdana', padding=5)
        height.grid(column=0, row=6, sticky='nw')

        #height variable
        height_value = StringVar()

        # height slider
        height_scale = Slider(SCREEN_HEIGHT, height_value)
        height_scale.scale.grid(column=0, row=7, sticky='nw', pady=10, padx=5)

        # height field
        height_field = Field(height_value)
        height_field.entry.grid(column=1, row=7)

        # width labels and sliders
        width = ttk.Label(root, text='The width of the box:', font='Verdana', padding=5)
        width.grid(column=0, row=8, sticky='nw', pady=10)

        #width variable
        width_value = StringVar()

        # width slider
        width_scale = Slider(SCREEN_HEIGHT, width_value)
        width_scale.scale.grid(column=0, row=9, sticky='nw', pady=10, padx=5)

        # width field
        width_field = Field(width_value)
        width_field.entry.grid(column=1, row=9)

        # delay label and sliders
        width = ttk.Label(root, text='The typing delay is:', font='Verdana', padding=5)
        width.grid(column=0, row=10, sticky='nw', pady=10)

        #delay variable
        delay_value = StringVar()

        # delay slider
        delay_scale = Slider(1.0, delay_value)
        delay_scale.scale.grid(column=0, row=11, sticky='nw', pady=10, padx=5)

        # delay field
        delay_field = Field(delay_value)
        delay_field.entry.grid(column=1, row=11, padx=10)


UserInterface(root)
root.mainloop()