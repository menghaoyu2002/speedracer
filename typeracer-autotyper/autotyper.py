"""
Autotyper for typeracer
adjust the x and y values as well as the bbox values so that the image
captures the typeracer text box well.

Works most of the time but sometimes it types too fast and misses some characters.
Reading wise it's pretty good.
"""
import pytesseract as pt
from PIL import ImageGrab, Image
import pyautogui
from typing import Optional


class AutoTyper:
    """A Class for an autotyper

    Instance Attributes:
        - x: the x coordinates of the top left corner of the image boxes
          (where you want to the image to start from on your screen)

        - y: the y coordinates of the top left corner of the image boxes
          (where you want to the image to start from on your screen)

        - height: the height of the box

        - width: the width of the box

    Note: the default values are set for typeracer on 125% zoom on 1920 x 1080
    """
    x: int
    y: int
    width: int
    height: int

    # Private Attributes
    _text: Optional[str] = None

    def __init__(self, x=450, y=600, width=1000, height=250) -> None:
        pt.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getImage(self) -> None:
        """Saves an image in the main folder for the program to read text off of"""
        screen = ImageGrab.grab(bbox=(self.x, self.y, self.width + self.x, self.height +self.y))
        screen.save('image.png')

    def readText(self) -> None:
        """Reads the text on image.png to a string"""
        self._text = pt.image_to_string(Image.open('image.png'))

        # filtering and replacing commonly wrong characters
        self._text = self._text.replace("|", "I")
        self._text = self._text.replace("\n", " ")

    def printText(self):
        print(self._text)

    def type(self, delay: float) -> None:
        """Types out the text from image.png with a delay of <delay> (in seconds)
        with a default delay of 0.01
        """
        pyautogui.write(self._text, interval=delay)



