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

# Default x and y values
x = 450
y=600

pt.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

# capturing the screen as an image
screen = ImageGrab.grab(bbox=(x, y, 1000 + x, 250+y))
screen.save('image.png')

# reading the text on the screen to a string
text = pt.image_to_string(Image.open('image.png'))
print(text)

# filtering and replacing commonly wrong characters
while "|" in text:
    text = text.replace("|", "I")
while "\n" in text:
    text = text.replace("\n", " ")

# typing the string out
pyautogui.write(text, interval=0.01)



