from pathlib import Path
from tkinter import Frame, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets/frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class PageOne(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.pageone_image = PhotoImage(file=relative_to_assets("button_1.png"))
        image_button = Button(
            self,
            image=self.pageone_image, 
            command=lambda: controller.show_frame("StartPage")
        )
        image_button.place(
            x=69.0,
            y=111.0,
            width=255.0,
            height=78.0
        )