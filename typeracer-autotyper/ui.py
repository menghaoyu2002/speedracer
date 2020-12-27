"""
This module deals with all the UI features
"""
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageGrab, ImageOps
from autotyper import AutoTyper

class Slider:
    def __init__(self, max, variable) -> None:
        self.scale = ttk.Scale(root, orient=HORIZONTAL, length=250, from_=0.0, to=max, variable=variable)


class Field:
    def __init__(self, variable) -> None:
        self.entry = ttk.Entry(root, textvariable=variable, width=7, font="Verdana")


class UserInterface:
    def __init__(self, root) -> None:
        root.title('Typeracer AutoTyper')
        previewframe = ttk.Frame(root, padding=10)
        previewframe.place(x=500, y=75)

        # x label
        X = ttk.Label(root, text='x value of box position:', font='Verdana', padding=10)
        X.grid(column=0, row=0, sticky='nw')

        # x variable
        self.x_value = IntVar()

        # x slider
        x_scale = Slider(SCREEN_WITDTH, self.x_value)
        x_scale.scale.grid(columnspan=2, column=0, row=1, sticky='nw', pady=10, padx=5)

        # x entry field
        x_field = Field(self.x_value)
        x_field.entry.grid(column=1, row=1, padx=5)

        # y labels
        Y = ttk.Label(root, text='y value of box position:', font='Verdana', padding=5)
        Y.grid(column=0, row=4, sticky='nw')

        # y variable
        self.y_value = IntVar()

        # y sliders
        y_scale = Slider(SCREEN_HEIGHT, self.y_value)
        y_scale.scale.grid(column=0, row=5, sticky='nw', pady=10, padx=5)

        # y entry field
        y_field = Field(self.y_value)
        y_field.entry.grid(column=1, row=5, padx=5)

        # height labels
        height = ttk.Label(root, text='The height of the box:', font='Verdana', padding=5)
        height.grid(column=0, row=6, sticky='nw')

        #height variable
        self.height_value = IntVar()

        # height slider
        height_scale = Slider(SCREEN_HEIGHT, self.height_value)
        height_scale.scale.grid(column=0, row=7, sticky='nw', pady=10, padx=5)

        # height field
        height_field = Field(self.height_value)
        height_field.entry.grid(column=1, row=7,padx=5)

        # width labels
        width = ttk.Label(root, text='The width of the box:', font='Verdana', padding=5)
        width.grid(column=0, row=8, sticky='nw', pady=10)

        #width variable
        self.width_value = IntVar()

        # width slider
        width_scale = Slider(SCREEN_WITDTH, self.width_value)
        width_scale.scale.grid(column=0, row=9, sticky='nw', pady=10, padx=5)

        # width field
        width_field = Field(self.width_value)
        width_field.entry.grid(column=1, row=9, padx=5)

        # delay label and sliders
        width = ttk.Label(root, text='The typing delay is:', font='Verdana', padding=5)
        width.grid(column=0, row=10, sticky='nw', pady=10)

        #delay variable
        self.delay_value = StringVar()

        # delay slider
        delay_scale = Slider(1.0, self.delay_value)
        delay_scale.scale.grid(column=0, row=11, sticky='nw', pady=10, padx=5)

        # delay field
        delay_field = Field(self.delay_value)
        delay_field.entry.grid(column=1, row=11, padx=5)

        #creates a canvas for preview
        self.canvas = Canvas(previewframe, width=500, height=300)
        self.canvas.grid(sticky='E')

        preview_button = Button(root, text="See Preview", command=self.load_preview, height=1, width=15, font="Verdana", border=5 )
        preview_button.grid(column=0, row=16, sticky='nw', padx=10, pady=10)


        start_button = Button(root, text="Run AutoTyper", command=self.type, height=1, width=15, font="Verdana", border=5 )
        start_button.grid(column=0, row=13, sticky='nw', padx=10, pady=10)

    def type(self) -> None:
        """Type the text on typeracer out"""
        autotyper = AutoTyper(self.x_value.get(), self.y_value.get(),
                              self.width_value.get(), self.height_value.get())
        autotyper.getImage()
        autotyper.readText()
        autotyper.type(delay = float(self.delay_value.get()))

    def load_preview(self):
        self.canvas.delete('all')
        image = ImageGrab.grab(bbox=(self.x_value.get(), self.y_value.get(),
                                     self.width_value.get() + self.x_value.get(),
                                     self.height_value.get() + self.y_value.get()))

        image.save('image.png')

        image = Image.open('image.png')
        image = ImageOps.fit(image, (500, 300))
        image.save('resized.png')
        screen = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor='center', image=screen)
        self.canvas.image = screen
        print('showing preview now')


if __name__ == '__main__':
    root = Tk()

    # root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(900, 550))
    # constants
    SCREEN_WITDTH = root.winfo_screenwidth()
    SCREEN_HEIGHT = root.winfo_screenheight()

    UserInterface(root)
    root.mainloop()