from tkinter import Frame
from gui.main import Main
from gui.recommend_calendar import RecommendCalendar 
from gui.recommend_style import RecommendStyle 
from gui.recommend_result import RecommendResult
from gui.style_list import StyleList
from gui.save_style import SaveStyle

# 화면 크기 (상수)
WINDOW_WIDTH = 375
WINDOW_HEIGHT = 812

class Controller:
    def __init__(self, root):
        self.root = root
        self.root.title("미경의 스타일기")
        self.root.geometry("%dx%d" % (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.root.configure(bg="#FFCBDD")

        # 화면 Frame들에서 공용으로 사용할 전역 변수
        self.recommend_date = None
        self.recommend_style = None
        self.style_index = None

        container = Frame(self.root)
        container.pack(side="top", fill="both", expand=True)

        # 화면 Frame들을 관리할 Dictionary
        self.frames = {}
        
        # for문으로 Frame 객체 접근
        for F in (Main, RecommendCalendar, RecommendStyle, RecommendResult, StyleList, SaveStyle):
            page_name = F.__name__
            frame = F(parent=container, controller=self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("Main")

    # Frame에서 공용으로 사용할 전역 함수
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def set_recommend_date(self, date):
        self.recommend_date = date
    
    def set_recommend_style(self, style): # tag
        self.recommend_style = style
    
    def set_style_index(self, style_index):
        self.style_index = style_index