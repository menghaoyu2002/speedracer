from autotyper import AutoTyper
from ahk import AHK
from typing import Optional

ahk = AHK()
autotyper = AutoTyper()

def type(typer: AutoTyper, delay: Optional[int] = 0.01) -> None:
    """ Types the text out"""
    typer.getImage()
    typer.readText()
    typer.type(delay = delay)

run = True
while run:
    if ahk.key_state("Pause"):
        type(autotyper)


