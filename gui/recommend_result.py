from tkinter import Frame, PhotoImage, Label
from utils.utils import get_assets_path, CustomCanvas, load_custom_font
from datetime import datetime, date
import calendar

ASSETS_PATH = get_assets_path("/recommend_result")

BACKGROUND_IMAGE_PATH = get_assets_path("/common/background.png")
TITLE_IMAGE_PATH = ASSETS_PATH / "title.png"

SAVE_INSTRUCTIONS_IMAGE_PATH = ASSETS_PATH / "save_Instructions.png"

SAVE_IMAGE_PATH = ASSETS_PATH / "save_button.png"
MOVE_IMAGE_PATH = ASSETS_PATH / "move_button.png"
RETRY_IMAGE_PATH = ASSETS_PATH / "retry_button.png"

class RecommendResult(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.canvas = CustomCanvas(self, width=width, height=height)

        self.isSave = False

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

        self.save_button_image = PhotoImage(file=SAVE_IMAGE_PATH)
        self.move_button_image = PhotoImage(file=MOVE_IMAGE_PATH)
        self.result_button = self.canvas.create_image(
            20.0 + 263.0 / 2,
            714.0,
            image=self.save_button_image
        )
        self.canvas.tag_bind(self.result_button, "<Button-1>", lambda e: self.button_event_handler("save"))

        self.retry_button_image = PhotoImage(file=RETRY_IMAGE_PATH)    
        self.retry_button = self.canvas.create_image(
            295.0 + 60.0 / 2,
            713.0,
            image=self.retry_button_image
        )
        self.canvas.tag_bind(self.retry_button, "<Button-1>", lambda e: self.button_event_handler("retry"))

    def button_event_handler(self, type):
        print(type)
        if type == 'save':
            self.save_lnstructions_image = PhotoImage(file=SAVE_INSTRUCTIONS_IMAGE_PATH)    
            self.save_lnstructions = self.canvas.create_image(
                375 / 2,
                660.0,
                image=self.save_lnstructions_image,
                tag="save"
            )
            self.canvas.itemconfig(self.result_button, image=self.move_button_image)
            self.canvas.tag_unbind(self.result_button, "<Button-1>")
            self.canvas.tag_bind(self.result_button, "<Button-1>", lambda e: self.button_event_handler("move"))
        elif type == 'move':
            self.controller.show_frame("StyleList")
            self.reset()
        elif type == 'retry':
            self.controller.show_frame("Main")
            self.reset()

    def reset(self):
        self.canvas.delete("save")
        self.canvas.itemconfig(self.result_button, image=self.save_button_image)
        self.canvas.tag_unbind(self.result_button, "<Button-1>")
        self.canvas.tag_bind(self.result_button, "<Button-1>", lambda e: self.button_event_handler("save"))
        self.controller.recommend_date = None
        self.controller.recommend_style = None

            
    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        print("aaaa")
        # self.update_data_from_server()
