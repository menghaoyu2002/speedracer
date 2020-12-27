# Typeracer Autotyper
Autotyper for typeracer. Works just as the name implies. 
It reads text from an area of your screen and then types it out upon request.
Can typeauto anything but specifically designed for typeracer. 

Note: I do not condone cheating. This was just a mini project I did while messing around with python libraries. All testing was done in a private Typeracer lobby.
Use at your own discretion.

# Dependencies / Libraries Used
This project uses the Pillow Library to capture images and the Tesseract/Pytesseract to read the text on the images.\
the "Keyboard" library is used to type out the words and to catch keyboard inputs. Tkinter is used for the GUI.

Note: If program doesn't run try specifying the Tesseract path in autotyper.py line 40 so that it corresponds with your own.

# Instructions for Usage

<ol>
  <li> Click on the "main.py" file to open up the program UI </br> <br/> </li>
  
<li> Adjust the sliders or enter in values for the x, y, height, and width settings so that the program is able to capture
  the Typeracer text box (or any text you want typed out for that matter).</br> <br/> </li> 
  
 <li> Click the "See Preview" Button to see if you've aligned the box correctly </br> <br/></li>   

 <li> Click the "Run Program" button to start the program. The program will wait until you press the Autotype key. 
  By default it's F12 but you can rebind it with change keybind button </br> <br/></li> 
  
 <li> Press the Autotype key and the Program will start typing. Press the Escape key to exist run mode </br> <br/></li> 
 </ol>


To Rebind the Autotype key simply press the "Change Keybind" button and press the desired keybind.

### [Demonstration of Autotyper](https://www.youtube.com/watch?v=4qUObfZtN9Y&feature=youtu.be)
