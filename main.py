import tkinter as tk
from tkinter import ttk
import settings
import time

# app_window configuration

app_win = tk.Tk()
app_win.geometry(settings.window_size)
app_win.title("Main app_window")
app_win.configure(bg=settings.bg_color)

# Methods

def show_score():
    time_spend = end_time - start_time
    time_label['text'] = f'time: {time_spend:0.2f}secs  '
    
    target = text_label['text']
    enter = text_entry.get()
    coincidence = 0
    for i in range(len(target)):
        if enter[i] == target[i]: coincidence += 1
    accuracy = (coincidence * 100) // len(target)
    accuracy_label['text'] = f'Accuracy: {accuracy}%  '

    wpm = (len(enter) / time_spend) * 60
    wpm_label['text'] = f'Wpm: {wpm:0.2f}  '

    info_panel.pack(side=tk.BOTTOM)


def comparison(event): 
    global end_time
    if len(text_label['text']) == len(text_entry.get()):
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
    text_entry.delete(0,tk.END)
    info_panel.pack_forget()
    sentence = 'A Brown Fox Jumped Over The Lazy Dogs quickly'
    start_time = time.perf_counter()
    text_label['text'] = sentence
    text_entry.focus()

# Placing Widgets

title = tk.Label(app_win, text='Typing Speed Test', foreground=settings.font_color, 
                background=app_win['bg'], font=settings.title_font)
title.pack(side=tk.TOP, pady=40)

text_label = tk.Label(app_win, text='Tap the button to start', foreground=settings.font_color, 
                background=app_win['bg'], font=settings.text_font)
text_label.pack(side=tk.TOP, pady=10)

text_entry = tk.Entry(app_win, width=50, font=settings.input_font, bg=app_win["bg"],
                      justify=tk.CENTER, bd=10, relief=tk.FLAT, highlightcolor=settings.font_color,
                      state= "disabled", disabledbackground=app_win["bg"], disabledforeground=settings.dis_color)
text_entry.pack(side=tk.TOP, pady=20)
text_entry.bind('<KeyPress>',comparison)

start_button = tk.Button(app_win, text = 'Start', width=8, height=2, bd=0, command=countdown)
start_button.pack(side=tk.BOTTOM, pady=20)

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