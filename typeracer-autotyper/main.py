from autotyper import AutoTyper
from ahk import AHK

ahk = AHK()
autotyper = AutoTyper()

def type(typer: AutoTyper) -> None:
    """ Types the text out"""
    typer.getImage()
    typer.readText()
    typer.type(0.015)

run = True
while run:
    if ahk.key_state("Pause"):
        type(autotyper)


