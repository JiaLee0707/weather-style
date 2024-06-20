import tkinter as tk
from gui.controller import Controller
from db import db

if __name__ == "__main__":
    # DB Connection
    db.connect()

    # Main window constructor
    root = tk.Tk()  # Make temporary window for app to start
    app = Controller(root)

    root.mainloop()
