"""
This module runs the autotyper.
Change the delay to your own preference.
Make sure all libraries are downloaded
"""
from autotyper import AutoTyper
from ahk import AHK
from typing import Optional

ahk = AHK()
autotyper = AutoTyper()

def type(typer: AutoTyper, delay: Optional[int] = 0.01) -> None:
    """Type the text on typeracer out"""
    typer.getImage()
    typer.readText()
    typer.type(delay = delay)


#######################################################################
#  Main Program Loop
#######################################################################
keybind = "Pause"  # default keybind to run script
run = True
while run:
    if ahk.key_state(keybind):
        type(autotyper)
    # keybind to end program
    if ahk.key_state("Escape"):
        run = False


