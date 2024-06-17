from pathlib import Path
from tkinter import Frame, Button, PhotoImage, Canvas, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets/main")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Main(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.canvas = Canvas(self, bg="#FFCBDD", width=width, height=height, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.background_check_image = PhotoImage(file=relative_to_assets("check.png"))    
        self.background_check = self.canvas.create_image(
            width/2,  # x 좌표
            height/2,  # y 좌표
            image=self.background_check_image
        )

        self.logo_image = PhotoImage(file=relative_to_assets("logo.png"))    
        self.logo = self.canvas.create_image(
            186.7265625,  # x 좌표
            199.16943359375,  # y 좌표
            image=self.logo_image
        )


        self.style_recommend_image = PhotoImage(file=relative_to_assets("style_recommend_button.png"))
        self.style_recommend_hover_image = PhotoImage(file=relative_to_assets("style_recommend_button_hover.png"))
        self.style_recommend = self.canvas.create_image(
            64.0 + 256.0 / 2,  # x 좌표
            455.0 + 31.0 / 2,  # y 좌표
            image=self.style_recommend_image
        )
        self.canvas.tag_bind(self.style_recommend, "<Button-1>", lambda e: self.style_recommend_event_handler("click"))
        self.canvas.tag_bind(self.style_recommend, "<Enter>", lambda e: self.style_recommend_event_handler("enter"))
        self.canvas.tag_bind(self.style_recommend, "<Leave>", lambda e: self.style_recommend_event_handler("leave"))
        

        self.style_list_image = PhotoImage(file=relative_to_assets("style_list_button.png"))
        self.style_list_hover_image = PhotoImage(file=relative_to_assets("style_list_button_hover.png"))
        self.style_list = self.canvas.create_image(
            64.0 + 256.0 / 2,  # x 좌표
            526.0 + 31.0 / 2,  # y 좌표
            image=self.style_list_image
        )
        self.canvas.tag_bind(self.style_list, "<Button-1>", lambda e: self.style_list_event_handler("click"))
        self.canvas.tag_bind(self.style_list, "<Enter>", lambda e: self.style_list_event_handler("enter"))
        self.canvas.tag_bind(self.style_list, "<Leave>", lambda e: self.style_list_event_handler("leave"))


    def style_recommend_event_handler(self, eventType):
        if eventType == 'click':
            self.controller.show_frame("Gui2")
        elif eventType == 'enter':
            self.canvas.itemconfig(self.style_recommend, image=self.style_recommend_hover_image)
        elif eventType == 'leave':
            self.canvas.itemconfig(self.style_recommend, image=self.style_recommend_image)

    def style_list_event_handler(self, eventType):
        if eventType == 'click':
            self.controller.show_frame("Gui2")
        elif eventType == 'enter':
            self.canvas.itemconfig(self.style_list, image=self.style_list_hover_image)
        elif eventType == 'leave':
            self.canvas.itemconfig(self.style_list, image=self.style_list_image)