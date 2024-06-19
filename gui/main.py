from tkinter import Frame, PhotoImage
from utils.utils import get_assets_path, CustomCanvas

ASSETS_PATH = get_assets_path("/main")

LOGO_IMAGE_PATH = ASSETS_PATH / "logo.png"
RECOMMEND_BUTTON_IMAGE_PATH = ASSETS_PATH / "style_recommend_button.png"
RECOMMEND_BUTTON_HOVER_IMAGE_PATH = ASSETS_PATH / "style_recommend_button_hover.png"

LIST_BUTTON_IMAGE_PATH = ASSETS_PATH / "style_list_button.png"
LIST_BUTTON_HOVER_IMAGE_PATH = ASSETS_PATH / "style_list_button_hover.png"

class Main(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.canvas = CustomCanvas(self, width, height)
        self.draw_screen()

    def draw_screen(self):
        self.logo_image = PhotoImage(file=LOGO_IMAGE_PATH)    
        self.logo = self.canvas.create_image(
            186.7265625,  # x 좌표
            199.16943359375,  # y 좌표
            image=self.logo_image
        )

        self.style_recommend_image = PhotoImage(file=RECOMMEND_BUTTON_IMAGE_PATH)
        self.style_recommend_hover_image = PhotoImage(file=RECOMMEND_BUTTON_HOVER_IMAGE_PATH)
        self.style_recommend_button = self.canvas.create_image(
            64.0 + 256.0 / 2,  # x 좌표
            455.0 + 31.0 / 2,  # y 좌표
            image=self.style_recommend_image
        )
        self.canvas.tag_bind(self.style_recommend_button, "<Button-1>", lambda e: self.style_recommend_button_event_handler("click"))
        self.canvas.tag_bind(self.style_recommend_button, "<Enter>", lambda e: self.style_recommend_button_event_handler("enter"))
        self.canvas.tag_bind(self.style_recommend_button, "<Leave>", lambda e: self.style_recommend_button_event_handler("leave"))
        
        self.style_list_image = PhotoImage(file=LIST_BUTTON_IMAGE_PATH)
        self.style_list_hover_image = PhotoImage(file=LIST_BUTTON_HOVER_IMAGE_PATH)
        self.style_list_button = self.canvas.create_image(
            64.0 + 256.0 / 2,  # x 좌표
            526.0 + 31.0 / 2,  # y 좌표
            image=self.style_list_image
        )
        self.canvas.tag_bind(self.style_list_button, "<Button-1>", lambda e: self.style_list_button_event_handler("click"))
        self.canvas.tag_bind(self.style_list_button, "<Enter>", lambda e: self.style_list_button_event_handler("enter"))
        self.canvas.tag_bind(self.style_list_button, "<Leave>", lambda e: self.style_list_button_event_handler("leave"))


    def style_recommend_button_event_handler(self, eventType):
        if eventType == 'click':
            self.controller.show_frame("RecommendCalendar")
        elif eventType == 'enter':
            self.canvas.itemconfig(self.style_recommend_button, image=self.style_recommend_hover_image)
        elif eventType == 'leave':
            self.canvas.itemconfig(self.style_recommend_button, image=self.style_recommend_image)

    def style_list_button_event_handler(self, eventType):
        if eventType == 'click':
            self.controller.show_frame("StyleList")
        elif eventType == 'enter':
            self.canvas.itemconfig(self.style_list_button, image=self.style_list_hover_image)
        elif eventType == 'leave':
            self.canvas.itemconfig(self.style_list_button, image=self.style_list_image)