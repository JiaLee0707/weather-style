from tkinter import Frame, PhotoImage, Label, Canvas, Scrollbar
from utils.utils import get_assets_path, CustomCanvas, load_custom_font
from db import db

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

        self.scrollable_frame = Frame(self, width=width - 20, height=300, bg="white", highlightthickness=0)
        self.scrollable_frame.place(x=20, y=110)

        self.scrollable_canvas = Canvas(self.scrollable_frame, width=width - 50, height=height - 250, bg="white", highlightthickness=0)
        self.scrollable_canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.scrollable_frame, orient="vertical", command=self.scrollable_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = Frame(self.scrollable_canvas, bg="white")
        self.scrollable_canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.inner_frame.bind("<Enter>", self.bind_mouse_scroll)
        self.inner_frame.bind("<Leave>", self.unbind_mouse_scroll)

        self.scrollable_canvas.bind("<Configure>", self.on_frame_configure)

        self.topImage = []
        self.topImageIndex = 0

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

        styleList = db.getStyleList()

        if len(styleList) <= 0:
            self.notting_saved_image = PhotoImage(file=NOTHING_SAVED_IMAGE_PATH)    
            self.noting_saved = self.canvas.create_image(
                375.0 / 2,
                400.0,
                image=self.notting_saved_image
            )
        else:

            self.images = []  # 이미지 객체를 저장할 리스트
            matchingDateSet = sorted(set([styleInfo.get("matching_date") for styleInfo in styleList]), reverse=True)
            row = 0

            for matchingDate in matchingDateSet:
                mathcingDateStyleList = [styleInfo for styleInfo in styleList if styleInfo.get("matching_date") == matchingDate]

                date_font = load_custom_font(24, "bold")
                date = Label(self.inner_frame, text=matchingDate.strftime("%Y.%m.%d"), font=date_font, bg="#FFFFFF", fg="black")
                date.grid(row=row, column=0, columnspan=1, padx=0, pady=5) 
                row += 1

                col = 0
                for i in range(len(mathcingDateStyleList)):
                    self.topImage = PhotoImage(file=mathcingDateStyleList[i].get('image_path')).subsample(8, 8)
                    self.bottomImage = PhotoImage(file=mathcingDateStyleList[i].get('bottom.image_path')).subsample(10, 10)
                    
                    self.frame = Canvas(self.inner_frame, bg="#FFFFFF", bd=2, relief="solid")
                    self.contents_label = Label(self.frame, image=self.topImage, bg="#ffffff", width=147, height=100)
                    self.contents_label.image = self.topImage
                    self.contents_label2 = Label(self.frame, image=self.bottomImage, bg="#ffffff", width=147, height=100)
                    self.contents_label2.image = self.bottomImage
                    self.contents_label.pack(padx=0, pady=0)
                    self.contents_label2.pack(padx=0, pady=0)

                    self.images.append(self.topImage)
                    self.images.append(self.bottomImage)

                    self.frame.grid(row=row, column=col, padx=5, pady=5)
                    self.contents_label.bind("<Button-1>", lambda e, styleIndex=mathcingDateStyleList[i].get('id'): self.style_button_event_handler(styleIndex))
                    self.contents_label2.bind("<Button-1>", lambda e, styleIndex=mathcingDateStyleList[i].get('id'): self.style_button_event_handler(styleIndex))

                    col += 1
                    if col == 2: 
                        row += 1
                        col = 0
                row += 1

        self.recommend_button_image = PhotoImage(file=RECOMMEND_IMAGE_PATH)
        self.recommend_button = self.canvas.create_image(
            375.0 / 2,
            714.0,
            image=self.recommend_button_image
        )
        self.canvas.tag_bind(self.recommend_button, "<Button-1>", lambda e: self.button_event_handler())

    def button_event_handler(self):
        self.controller.show_frame("RecommendCalendar")
        self.reset()

    def reset(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
            
        self.canvas.delete("date")
        self.canvas.delete("contents")
        
    def style_button_event_handler(self, styleIndex) :
        self.controller.set_style_index(styleIndex)
        self.controller.show_frame("SaveStyle")

    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        self.draw_screen()
