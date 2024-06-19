import sys
import tkinter as tk
from pathlib import Path
import requests
from datetime import datetime

sys.path.append(str(Path(__file__).resolve().parent))

from pathlib import Path
from tkinter import Canvas, PhotoImage, font, Label

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def get_assets_path(file_name: str, type="image") -> Path:
    return ASSETS_PATH / Path(type + file_name)

# 프로젝트 폰트 파일 경로
DEFAULT_FONT_PATH = get_assets_path("/ONE Mobile POP OTF.otf", "font")  # 폰트 파일 경로

default_font = None

def load_custom_font(size=24, weight="bold"):
    font_path_str = str(DEFAULT_FONT_PATH)
    # print(DEFAULT_FONT_PATH)
    if not Path(font_path_str).exists():
        raise FileNotFoundError(f"Font file not found: {font_path_str}")

    # Register the font
    # tk._default_root.tk.call('font', 'create', 'OneMobilePopFont', '-family', 'ONE Mobile POP', '-size', '100')

    # Create a custom font object
    custom_font = tk.font.Font(family="ONE Mobile POP", size=size, weight=weight)
    return custom_font


def get_current_temperature(date):
    api_key = '243a864f8a027704f94f8c945a071854'
    city_name = "Seoul"
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&q={city_name}&appid={api_key}&lang=kr&units=metric"

    response = requests.get(api_url)
    data = response.json()
    
    matching_date = datetime.strptime(date, "%Y-%m-%d")
    
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    current_date = datetime.strptime(formatted_date, "%Y-%m-%d")

    date_difference = matching_date - current_date

    index = date_difference.days

    return data['list'][index]['main']["temp"]

class CustomCanvas(Canvas):
    def __init__(self, parent, width, height, bg_color="#FFCBDD"):
        super().__init__(parent, bg=bg_color, width=width, height=height, bd=0, highlightthickness=0)
        self.place(x=0, y=0)

        self.background_image = PhotoImage(file=get_assets_path('/common/check.png'))
        self.create_image(width/2, height/2, image=self.background_image)

        # self.custom_font = self.load_custom_font()