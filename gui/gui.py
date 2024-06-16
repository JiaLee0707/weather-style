from tkinter import Frame
from gui.gui1 import StartPage
from gui.gui2 import PageOne

WINDOW_WIDTH = 394
WINDOW_HEIGHT = 628

class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Main App")
        self.root.geometry("%dx%d" % (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.root.configure(bg="#FFFFFF")

        container = Frame(self.root)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # for frame in self.frames.values():
        #     frame.forget()

        frame = self.frames[page_name]
        frame.tkraise()
