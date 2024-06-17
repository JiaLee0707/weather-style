from pathlib import Path
from tkinter import Frame, Button, PhotoImage, Canvas, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets/home")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Gui2(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        # self.configure(width=width, height=height)

        self.canvas = Canvas(self, bg="#ffffff", width=width, height=height, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)