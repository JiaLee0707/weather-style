from tkinter import Frame
from gui.main import Main
from gui.recommend import Recommend

WINDOW_WIDTH = 375
WINDOW_HEIGHT = 812

class Controller:
    def __init__(self, root):
        self.root = root
        self.root.title("미경의 스타일기")
        self.root.geometry("%dx%d" % (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.root.configure(bg="#FFCBDD")

        container = Frame(self.root)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        
        for F in (Main, Recommend):
            page_name = F.__name__
            frame = F(parent=container, controller=self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Recommend")

    def show_frame(self, page_name):
        # for frame in self.frames.values():
        #     frame.forget()

        frame = self.frames[page_name]
        frame.tkraise()
