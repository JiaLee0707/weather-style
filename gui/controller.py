from tkinter import Frame
from gui.main import Main
from gui.recommend_calendar import RecommendCalendar 
from gui.recommend_style import RecommendStyle 
from gui.recommend_result import RecommendResult
from gui.style_list import StyleList
from gui.save_style import SaveStyle

WINDOW_WIDTH = 375
WINDOW_HEIGHT = 812

class Controller:
    def __init__(self, root):
        self.root = root
        self.root.title("미경의 스타일기")
        self.root.geometry("%dx%d" % (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.root.configure(bg="#FFCBDD")

        self.recommend_date = None
        self.recommend_style = None

        container = Frame(self.root)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        
        for F in (Main, RecommendCalendar, RecommendStyle, RecommendResult, StyleList, SaveStyle):
            page_name = F.__name__
            frame = F(parent=container, controller=self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("SaveStyle")

    def show_frame(self, page_name):
        # for frame in self.frames.values():
        #     frame.forget()

        frame = self.frames[page_name]
        frame.tkraise()

    def set_recommend_date(self, date):
        self.recommend_date = date
    
    def set_recommend_style(self, style): # tag
        self.recommend_style = style