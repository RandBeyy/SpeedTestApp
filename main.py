import tkinter as tk
from tkinter import ttk
from settings import Settings
import time
from random import choice
import csv

settings = Settings()
# app_window configuration

app_win = tk.Tk()
app_win.geometry(settings.window_size)
app_win.title("Main app_window")
app_win.configure(bg=settings.bg_color)

# Methods


def show_score():
    time_spend = end_time - start_time
    if time_spend > 30: time_label['fg'] = settings.red_col
    else: time_label['fg'] = settings.font_color
    time_label['text'] = f'Time: {time_spend:0.2f}secs  '

    target = text_label['text']
    enter = text_entry.get()
    coincidence = 0
    for i in range(len(enter)):
        if enter[i] == target[i]: coincidence += 1
    accuracy = (coincidence * 100) // len(target)
    if accuracy < 50: accuracy_label['fg'] = settings.red_col
    else: accuracy_label['fg'] = settings.font_color
    accuracy_label['text'] = f'Accuracy: {accuracy}%  '

    wpm = (len(enter) / time_spend) * 60
    if wpm < 100: wpm_label['fg'] = settings.red_col
    else: wpm_label['fg'] = settings.font_color
    wpm_label['text'] = f'Wpm: {wpm:0.2f}  '

    info_panel.pack(side=tk.BOTTOM)


def comparison(event: tk.Event): 
    global end_time
    if len(text_label['text']) == len(text_entry.get()) or event.keycode == 603979789:
        end_time = time.perf_counter()
        text_entry['state'] = 'disabled'
        app_win.focus()
        show_score()


def countdown(count=settings.countdown):
    label_counter['text'] = count
    if count > 0:
        app_win.after(1000, countdown, count-1)
    else: 
        label_counter['text'] = ''
        start_typing()


def start_typing():
    global start_time
    text_entry['state'] = "normal"
    text_entry.delete(0, tk.END)
    info_panel.pack_forget()
    sentence = choice(settings.quotes)
    start_time = time.perf_counter()
    text_label['text'] = sentence
    text_entry.focus()

# Placing Widgets

title = tk.Label(app_win, text='Typing Speed Test', foreground=settings.font_color, 
                background=app_win['bg'], font=settings.title_font)
title.pack(side=tk.TOP, pady=settings.title_pady)

text_label = tk.Label(app_win, text='Tap the button to start', foreground=settings.font_color, 
                background=app_win['bg'], font=settings.text_font)
text_label.pack(side=tk.TOP, pady=settings.text_label_pady)

text_entry = tk.Entry(app_win, width=settings.text_entry_width, font=settings.input_font, 
                      bg=app_win["bg"], justify=tk.CENTER, bd=settings.text_entry_bd, 
                      relief=tk.FLAT, highlightcolor=settings.font_color, state= "disabled", 
                      disabledbackground=app_win["bg"], disabledforeground=settings.disabled_color)
text_entry.pack(side=tk.TOP, pady=settings.text_entry_pady)
text_entry.bind('<KeyPress>', comparison)

hint_label = tk.Label(app_win, text='When finish typing or to terminate press Enter', foreground=settings.font_color, 
                background=app_win['bg'], font=settings.input_font)
hint_label.pack(side=tk.TOP, pady=settings.hint_label_pady)

start_button = tk.Button(app_win, text = 'Start', width=settings.start_button_width, 
                        height=settings.start_button_height, bd=settings.start_button_bd, 
                        command=countdown)
start_button.pack(side=tk.BOTTOM, pady=settings.start_button_pady)

label_counter = tk.Label(app_win, foreground=settings.font_color, 
                background=app_win['bg'], font=settings.title_font)
label_counter.pack(side=tk.BOTTOM)

info_panel = tk.PanedWindow(orient ='horizontal')
time_label = tk.Label(info_panel, foreground=settings.font_color, 
                background=app_win['bg'], font=settings.text_font)
accuracy_label = tk.Label(info_panel, foreground=settings.font_color, 
                background=app_win['bg'], font=settings.text_font)
wpm_label = tk.Label(info_panel, foreground=settings.font_color, 
                background=app_win['bg'], font=settings.text_font)
info_panel.add(time_label)
info_panel.add(accuracy_label)
info_panel.add(wpm_label)

start_time = float()
end_time = float()



app_win.mainloop()