from tkinter import Frame, PhotoImage, Label
from utils.utils import get_assets_path, CustomCanvas, load_custom_font
from datetime import datetime, date
import calendar

ASSETS_PATH = get_assets_path("/recommend_calendar")

BACKGROUND_IMAGE_PATH = get_assets_path("/common/background.png")
TITLE_IMAGE_PATH = ASSETS_PATH / "title.png"

NEXT_BUTTON_DISABLED_IMAGE_PATH = get_assets_path("/common/next_button_disabled.png")
NEXT_BUTTON_IMAGE_PATH = get_assets_path("/common/next_button.png")

STAR_IMAGE_PATH = ASSETS_PATH / "star.png"

class RecommendCalendar(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.canvas = CustomCanvas(self, width=width, height=height)

        now = datetime.now()
        self.set_date(now)

        self.draw_screen()
    
    def set_date(self, now):
        self.current_date = now.strftime("%Y년 %m월").lstrip("0").replace(" 0", " ")

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

        date_font = load_custom_font(24, "bold")
        self.date = Label(self, text=self.current_date, font=date_font, bg="#FFFFFF", fg="black")
        self.date.place(x=30, y=250) 


        day_font = load_custom_font(22, "bold")
        index = 0
        day = ['일', '월', '화', '수', '목', '금', '토']
        for i in day:
            font_color = "black"
            if index == 0 or index == len(day) - 1:
                font_color = "#FF41A3"

            day_i = Label(self, text=i, font=day_font, bg="#FFFFFF", fg=font_color)
            day_i.place(x=30 + index * 47, y=300) 
            index += 1

        self.create_widgets()

    def create_widgets(self):
        day_font = load_custom_font(14, "bold")
        self.start_x = 25
        self.start_y = 340
        self.cell_width = 33
        self.cell_height = 30

        today = date.today()
        year = today.year
        month = today.month
        day_today = today.day

        calendar.setfirstweekday(calendar.SUNDAY)
        cal = calendar.monthcalendar(year, month)
        
        self.day_widgets = {}
        self.text_id = {}

        for week_index, week in enumerate(cal):
            for day_index, day in enumerate(week):
                if day == 0:
                    day_str = ""
                else:
                    day_str = str(day)

                x = self.start_x + day_index * self.cell_width * 1.44
                y = self.start_y + week_index * self.cell_height * 1.7

                isDisabled = False
                font_color = "black"
                if day_index == 0 or day_index == 6:
                    font_color = "#FF41A3"
                
                if day != 0 and not (day_today <= day <= day_today + 9):
                    isDisabled = True
                    if day_index == 0 or day_index == 6:
                        font_color = "#FFCCE6"
                    else:
                        font_color = "#DBDBDB"

                self.text_id[day_str] = self.canvas.create_text(x + self.cell_width // 2, y + self.cell_height // 2, text=day_str, fill=font_color, font=day_font)
        
                if day != 0 and not isDisabled:
                    self.canvas.tag_bind(self.text_id[day_str], "<Button-1>", lambda e, day=day, x=x, y=y: self.date_button_event_handler(day, x, y))
                    self.day_widgets[day_str] = (self.text_id[day_str], x, y)  # 날짜별로 좌표를 저장

        # self.canvas.create_text(self.start_x, self.start_y - self.cell_height, anchor="nw", text=f"{year}년 {month}월", font=day_font)

    def date_button_event_handler(self, day, x, y):
        day_font = load_custom_font(14, "bold")

        if self.controller.recommend_date is not None:
            print(self.controller.recommend_date["day"])
            selected_day = str(self.controller.recommend_date["day"])

            self.canvas.delete("star")
            self.canvas.delete("selected_day")

        self.canvas.itemconfig(self.next_button, image=self.next_button_image)
        # 스타 이미지 추가
        self.star_image = PhotoImage(file=STAR_IMAGE_PATH)
        self.canvas.create_image(x + self.cell_width // 2, y + self.cell_height // 2, image=self.star_image, tags="star")

        self.canvas.create_text(x + self.cell_width // 2, y + self.cell_height // 2, text=str(day), fill="white", font=day_font, tags="selected_day")
        
        selected_day = {"day": day, "x": x, "y": y}
        self.controller.set_recommend_date(selected_day)


    def next_button_event_handler(self, eventType):
        if eventType == 'click':
            if self.controller.recommend_date is not None:
                self.controller.show_frame("RecommendStyle")
