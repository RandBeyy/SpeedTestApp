import tkinter as tk
from tkinter import ttk
import settings
import time

# app_window configuration

app_win = tk.Tk()
app_win.geometry(settings.window_size)
app_win.title("Main app_window")
app_win.configure(bg=settings.bg_color)

# Placing widgets

title = tk.Label(app_win, text='Typing Speed Test', foreground=settings.font_color, 
                background=app_win['bg'], font=settings.title_font)
title.pack(side=tk.TOP, pady=40)

text_label = tk.Label(app_win, text='Tap the button to start', foreground=settings.font_color, 
                background=app_win['bg'], font=settings.text_font)
text_label.pack(side=tk.TOP, pady=10)

text_entry = tk.Entry(app_win, width=50, font=settings.input_font, bg=app_win["bg"],
                      justify=tk.CENTER, bd=10, relief=tk.FLAT, highlightcolor=settings.font_color)
text_entry.pack(side=tk.TOP, pady=20)

def countdown(count):
    label_counter['text'] = count

    if count > 0:
        app_win.after(1000, countdown, count-1)
    else: label_counter['text'] = ''


def start_typing():
    countdown(3)
    


        

start_button = tk.Button(app_win, text = 'Start', width=8, height=2, bd=0, command=start_typing)
start_button.pack(side=tk.BOTTOM, pady=20)
label_counter = tk.Label(app_win, foreground=settings.font_color, 
                background=app_win['bg'], font=settings.title_font)
label_counter.pack(side=tk.BOTTOM)




app_win.mainloop()