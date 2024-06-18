from tkinter import Frame, PhotoImage, Label
from utils.utils import get_assets_path, CustomCanvas, load_custom_font
from datetime import datetime, date
import calendar

ASSETS_PATH = get_assets_path("/recommend")

BACKGROUND_IMAGE_PATH = ASSETS_PATH / "background.png"
TITLE_IMAGE_PATH = ASSETS_PATH / "title.png"

NEXT_BUTTON_DISABLED_IMAGE_PATH = ASSETS_PATH / "next_button_disabled.png"
NEXT_BUTTON_IMAGE_PATH = ASSETS_PATH / "next_button.png"

class Recommend(Frame):
    def __init__(self, parent, controller, width, height):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=width, height=height)

        self.canvas = CustomCanvas(self, width=width, height=height)

        now = datetime.now()
        self.set_date(now)

        # 원하는 형식으로 날짜를 포맷팅 (Windows 호환)

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
            712.0,
            image=self.next_button_disabled_image
        )
        self.canvas.tag_bind(self.next_button, "<Button-1>", lambda e: self.next_button_event_handler("click"))
        # self.canvas.tag_bind(self.next_button, "<Enter>", lambda e: self.next_button_event_handler("enter"))
        # self.canvas.tag_bind(self.next_button, "<Leave>", lambda e: self.next_button_event_handler("leave"))


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

        for week_index, week in enumerate(cal):
            for day_index, day in enumerate(week):
                if day == 0:
                    day_str = ""
                else:
                    day_str = str(day)

                x = self.start_x + day_index * self.cell_width * 1.44
                y = self.start_y + week_index * self.cell_height * 1.7

                font_color = "black"
                if day_index == 0 or day_index == 6:
                    font_color = "#FF41A3"
                
                # 사각형 그리기 조건 추가
                if day != 0 and not (day_today <= day <= day_today + 9):
                    if day_index == 0 or day_index == 6:
                        font_color = "#FFCCE6"
                    else:
                        font_color = "#DBDBDB"
                    #FFCCE6
                    # self.canvas.create_rectangle(x, y, x + self.cell_width, y + self.cell_height, fill="gray90", stipple="gray25", outline="")

                # 날짜 텍스트 추가
                self.canvas.create_text(x + self.cell_width // 2, y + self.cell_height // 2, text=day_str, fill=font_color, font=day_font)
        
        # 월과 연도 라벨
        self.canvas.create_text(self.start_x, self.start_y - self.cell_height, anchor="nw", text=f"{year}년 {month}월", font=day_font)


    def next_button_event_handler(self, eventType):
        if eventType == 'click':
            pass
            # self.controller.show_frame("Gui2")
        # elif eventType == 'enter':
        #     self.canvas.itemconfig(self.style_list_button, image=self.style_list_hover_image)
        # elif eventType == 'leave':
        #     self.canvas.itemconfig(self.style_list_button, image=self.style_list_image)

