from tkinter import Frame, PhotoImage, Label, Canvas, Scrollbar
from utils.utils import get_assets_path, CustomCanvas, load_custom_font
from datetime import datetime, date
import calendar

ASSETS_PATH = get_assets_path("/style_list")

BACKGROUND_IMAGE_PATH = get_assets_path("/common/background.png")
NOTHING_SAVED_IMAGE_PATH = ASSETS_PATH / "nothing_saved.png"

RECOMMEND_IMAGE_PATH = ASSETS_PATH / "recommend_button.png"

CONTENTS_IMAGE_PATH = ASSETS_PATH / "contents.png"

class StyleList(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.canvas = CustomCanvas(self, width=width, height=height)

        # 스크롤 가능한 영역을 포함하는 프레임 생성
        self.scrollable_frame = Frame(self, width=width - 20, height=300, bg="white", highlightthickness=0)  # 높이 300 설정, 배경색 흰색으로 설정
        self.scrollable_frame.place(x=20, y=110)  # y 위치를 100으로 설정

        # Canvas 생성
        self.scrollable_canvas = Canvas(self.scrollable_frame, width=width - 50, height=height - 250, bg="white", highlightthickness=0)  # 스크롤바를 위한 여유 공간 확보, 배경색 흰색으로 설정
        self.scrollable_canvas.pack(side="left", fill="both", expand=True)

        # 스크롤 가능한 프레임 생성
        self.inner_frame = Frame(self.scrollable_canvas, bg="white")  # 배경색 흰색으로 설정
        self.scrollable_canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.scrollable_canvas.bind("<Configure>", self.on_frame_configure)

        self.scrollbar = Scrollbar(self.scrollable_frame, orient="vertical", command=self.scrollable_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame.bind("<Enter>", self.bind_mouse_scroll)
        self.inner_frame.bind("<Leave>", self.unbind_mouse_scroll)

        self.draw_screen()

    def on_frame_configure(self, event=None):
        self.scrollable_canvas.configure(scrollregion=self.scrollable_canvas.bbox("all"))

    def bind_mouse_scroll(self, event):
        self.scrollable_canvas.bind_all("<MouseWheel>", self.on_mouse_scroll)

    def unbind_mouse_scroll(self, event):
        self.scrollable_canvas.unbind_all("<MouseWheel>")

    def on_mouse_scroll(self, event):
        self.scrollable_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def draw_screen(self):
        self.background_image = PhotoImage(file=BACKGROUND_IMAGE_PATH)    
        self.background = self.canvas.create_image(
            187.0,  # x 좌표
            479.0,  # y 좌표
            image=self.background_image
        )

        if False:
            self.notting_saved_image = PhotoImage(file=NOTHING_SAVED_IMAGE_PATH)    
            self.noting_saved = self.canvas.create_image(
                375.0 / 2,
                400.0,
                image=self.notting_saved_image
            )
        else:
            date_font = load_custom_font(24, "bold")
            self.date = Label(self.inner_frame, text="2024년 6월", font=date_font, bg="#FFFFFF", fg="black")
            self.date.grid(row=0, column=0, columnspan=1, pady=(20, 0)) 
            # self.date.pack(pady=(10, 0))
            self.contents_image = PhotoImage(file=CONTENTS_IMAGE_PATH)
            for i in range(10): 
                contents_label = Label(self.inner_frame, image=self.contents_image, bg="#FFFFFF")
                # contents_label.pack(pady=(30, i))
                contents_label.grid(row=(i // 2) + 1, column=i % 2, padx=5, pady=(10, 10))
                contents_label.grid(row=(i // 2) + 1, column=i % 2, padx=5, pady=(10, 10))
                # self.canvas.tag_bind(contents_label, "<Button-1>", lambda e: self.button_event_handler('style'))
            # pass

        self.recommend_button_image = PhotoImage(file=RECOMMEND_IMAGE_PATH)
        self.recommend_button = self.canvas.create_image(
            375.0 / 2,
            714.0,
            image=self.recommend_button_image
        )
        self.canvas.tag_bind(self.recommend_button, "<Button-1>", lambda e: self.button_event_handler('recommend'))

    def button_event_handler(self, type):
        if type == 'recommend':
            self.controller.show_frame("RecommendCalendar")
        elif type == 'style':
            # self.controller.set_recommend_date()
            # self.controller.set_recommend_style()
            
            self.controller.show_frame("SaveStyle")


    def reset(self):
        pass
