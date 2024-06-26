from tkinter import Frame, PhotoImage
from utils.utils import get_assets_path, CustomCanvas

ASSETS_PATH = get_assets_path("/recommend_style")

BACKGROUND_IMAGE_PATH = get_assets_path("/common/background.png")
TITLE_IMAGE_PATH = ASSETS_PATH / "title.png"

NEXT_BUTTON_DISABLED_IMAGE_PATH = get_assets_path("/common/next_button_disabled.png")
NEXT_BUTTON_IMAGE_PATH = get_assets_path("/common/next_button.png")

LOVELY_BUTTON_DISABLED_IMAGE_PATH = ASSETS_PATH / "lovely_button_disabled.png"
LOVELY_BUTTON_IMAGE_PATH = ASSETS_PATH / "lovely_button.png"

FEMININE_BUTTON_DISABLED_IMAGE_PATH = ASSETS_PATH / "feminine_button_disabled.png"
FEMININE_BUTTON_IMAGE_PATH = ASSETS_PATH / "feminine_button.png"

STREET_BUTTON_DISABLED_IMAGE_PATH = ASSETS_PATH / "street_button_disabled.png"
STREET_BUTTON_IMAGE_PATH = ASSETS_PATH / "street_button.png"

CASUAL_BUTTON_DISABLED_IMAGE_PATH = ASSETS_PATH / "casual_button_disabled.png"
CASUAL_BUTTON_IMAGE_PATH = ASSETS_PATH / "casual_button.png"

class RecommendStyle(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.canvas = CustomCanvas(self, width=width, height=height)

        self.draw_screen()
    
    def draw_screen(self):
        self.background_image = PhotoImage(file=BACKGROUND_IMAGE_PATH)    
        self.background = self.canvas.create_image(
            187.0,  # x 좌표
            479.0,  # y 좌표
            image=self.background_image
        )

        self.title_image = PhotoImage(file=TITLE_IMAGE_PATH)    
        self.title = self.canvas.create_image(
            134.0,
            176.0,
            image=self.title_image
        )

        self.next_button_disabled_image = PhotoImage(file=NEXT_BUTTON_DISABLED_IMAGE_PATH)    
        self.next_button_image = PhotoImage(file=NEXT_BUTTON_IMAGE_PATH)
        self.next_button = self.canvas.create_image(
            375.0 / 2,
            714.0,
            image=self.next_button_disabled_image
        )
        self.canvas.tag_bind(self.next_button, "<Button-1>", lambda e: self.next_button_event_handler("click"))

        # styles
        self.lovely_button_disabled_image = PhotoImage(file=LOVELY_BUTTON_DISABLED_IMAGE_PATH)    
        self.lovely_button_image = PhotoImage(file=LOVELY_BUTTON_IMAGE_PATH)    
        self.lovely_button = self.canvas.create_image(
            106.0,
            357.0,
            image=self.lovely_button_disabled_image
        )
        self.canvas.tag_bind(self.lovely_button, "<Button-1>", lambda e: self.style_button_event_handler("러블리"))
        

        self.feminine_button_disabled_image = PhotoImage(file=FEMININE_BUTTON_DISABLED_IMAGE_PATH)    
        self.feminine_button_image = PhotoImage(file=FEMININE_BUTTON_IMAGE_PATH)    
        self.feminine_button = self.canvas.create_image(
            268.0,
            357.0,
            image=self.feminine_button_disabled_image
        )
        self.canvas.tag_bind(self.feminine_button, "<Button-1>", lambda e: self.style_button_event_handler("페미닌"))


        self.street_button_disabled_image = PhotoImage(file=STREET_BUTTON_DISABLED_IMAGE_PATH)    
        self.street_button_image = PhotoImage(file=STREET_BUTTON_IMAGE_PATH)    
        self.street_button = self.canvas.create_image(
            106.0,
            513.0,
            image=self.street_button_disabled_image
        )
        self.canvas.tag_bind(self.street_button, "<Button-1>", lambda e: self.style_button_event_handler("스트릿"))


        self.casual_button_disabled_image = PhotoImage(file=CASUAL_BUTTON_DISABLED_IMAGE_PATH)    
        self.casual_button_image = PhotoImage(file=CASUAL_BUTTON_IMAGE_PATH)
        self.casual_button = self.canvas.create_image(
                268.0,
                513.0,
                image=self.casual_button_disabled_image
        )
        self.canvas.tag_bind(self.casual_button, "<Button-1>", lambda e: self.style_button_event_handler("캐주얼"))

        
    def style_button_event_handler(self, style):
        if self.controller.recommend_style is not None:
            self.canvas.itemconfig(self.lovely_button, image=self.lovely_button_disabled_image)
            self.canvas.itemconfig(self.feminine_button, image=self.feminine_button_disabled_image)
            self.canvas.itemconfig(self.street_button, image=self.street_button_disabled_image)
            self.canvas.itemconfig(self.casual_button, image=self.casual_button_disabled_image)

        if style == '러블리':
            self.canvas.itemconfig(self.lovely_button, image=self.lovely_button_image)
        elif style == '페미닌':
            self.canvas.itemconfig(self.feminine_button, image=self.feminine_button_image)
        elif style == '스트릿':
            self.canvas.itemconfig(self.street_button, image=self.street_button_image)
        elif style == '캐주얼':
            self.canvas.itemconfig(self.casual_button, image=self.casual_button_image)
                
        self.canvas.itemconfig(self.next_button, image=self.next_button_image)
        self.controller.set_recommend_style(style)


    def next_button_event_handler(self, eventType):
        if eventType == 'click':
            if self.controller.recommend_style is not None:
                self.controller.show_frame("RecommendResult")
                self.reset()

    def reset(self):
        self.canvas.itemconfig(self.lovely_button, image=self.lovely_button_disabled_image)
        self.canvas.itemconfig(self.feminine_button, image=self.feminine_button_disabled_image)
        self.canvas.itemconfig(self.street_button, image=self.street_button_disabled_image)
        self.canvas.itemconfig(self.casual_button, image=self.casual_button_disabled_image)
        self.canvas.itemconfig(self.next_button, image=self.next_button_disabled_image)
