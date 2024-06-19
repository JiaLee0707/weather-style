from tkinter import Frame, PhotoImage, Label
from utils.utils import get_assets_path, CustomCanvas, get_current_temperature, load_custom_font
import webbrowser
from db import db

ASSETS_PATH = get_assets_path("/recommend_result")

BACKGROUND_IMAGE_PATH = get_assets_path("/common/background.png")

SAVE_INSTRUCTIONS_IMAGE_PATH = ASSETS_PATH / "save_Instructions.png"

SAVE_IMAGE_PATH = ASSETS_PATH / "save_button.png"
MOVE_IMAGE_PATH = get_assets_path("/common/move_button.png")
BEFORE_IMAGE_PATH = get_assets_path("/common/before_button.png")

LINK_IMAGE_PATH = ASSETS_PATH / "link.png"

class SaveStyle(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.canvas = CustomCanvas(self, width=width, height=height)

        self.isSave = False
        
        self.recommendResult = None

        self.draw_screen()
        # self.draw_style_result()
    
    def draw_screen(self):

        self.background_image = PhotoImage(file=BACKGROUND_IMAGE_PATH)    
        self.background = self.canvas.create_image(
            187.0,  # x 좌표
            479.0,  # y 좌표
            image=self.background_image
        )

        self.move_button_image = PhotoImage(file=MOVE_IMAGE_PATH)
        self.move_button = self.canvas.create_image(
            20.0 + 263.0 / 2,
            714.0,
            image=self.move_button_image
        )
        self.canvas.tag_bind(self.move_button, "<Button-1>", lambda e: self.button_event_handler("move"))

        self.before_button_image = PhotoImage(file=BEFORE_IMAGE_PATH)    
        self.before_button = self.canvas.create_image(
            295.0 + 60.0 / 2,
            713.0,
            image=self.before_button_image
        )
        self.canvas.tag_bind(self.before_button, "<Button-1>", lambda e: self.button_event_handler("before"))

    def button_event_handler(self, type):
        if type == 'move':
            self.controller.show_frame("StyleList")
            # self.reset()
        elif type == 'before':
            self.controller.show_frame("Main")
            # self.reset()

    def reset(self):
        self.canvas.delete("styleBottom")
        self.canvas.delete("styleTop")
        # self.controller.recommend_date = None
        # self.controller.recommend_style = None

    def draw_style_result(self): 
        # 아이디 값 변경 필요 !!!!!
        self.styleResult = db.getStyleById(1)

        title_font = load_custom_font(27, "bold")
        title = Label(self, text=self.styleResult.get('matching_date').strftime("%Y/%m/%d"), font=title_font, bg="#FFFFFF", fg="black")
        title.place(x=30, y=135) 
        title_font = load_custom_font(27, "bold")
        title = Label(self, text="추천받은 코디야!", font=title_font, bg="#FFFFFF", fg="black")
        title.place(x=30, y=175) 
        
        self.styleBottomImage = PhotoImage(file=self.styleResult.get('bottom.image_path')).subsample(4, 4)
        self.styleBottom = self.canvas.create_image(
            220.0,  # x 좌표
            500.0,  # y 좌표
            image = self.styleBottomImage,
            tags="styleBottom"
        )

        self.styleTopImage = PhotoImage(file=self.styleResult.get('image_path')).subsample(4, 4)
        self.styleTop = self.canvas.create_image(
            160.0,  # x 좌표
            350.0,  # y 좌표
            image = self.styleTopImage,
            tags="styleTop"
        )


        self.styleLTopLinkImage = PhotoImage(file=LINK_IMAGE_PATH)
        self.styleTopLink = self.canvas.create_image(
            222.0,  # x 좌표
            280.0,  # y 좌표
            image = self.styleLTopLinkImage,
            tags="styleTopLink"
        )
        self.canvas.tag_bind(self.styleTopLink, "<Button-1>", lambda e: self.open_webbrowser(self.styleResult.get('link')))
        
        self.styleBottomLinkImage = PhotoImage(file=LINK_IMAGE_PATH)
        self.styleBottomLink = self.canvas.create_image(
            290.0,  # x 좌표
            510.0,  # y 좌표
            image = self.styleBottomLinkImage,
            tags="styleBottomLink"
        )
        self.canvas.tag_bind(self.styleBottomLink, "<Button-1>", lambda e: self.open_webbrowser(self.styleResult.get('bottom.link')))
        
    def open_webbrowser(self, url):
        webbrowser.open_new(url)
            
    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        self.draw_style_result()
