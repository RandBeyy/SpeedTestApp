class Settings:
    def __init__(self):

        # Main window settings:
        self.window_size = "700x500"
        self.bg_color = "#2b2d42"

        # Colors:
        self.font_color = "#EDF2F4"
        self.disabled_color = "#8D99AE"
        self.red_col = "#EF233C"
        
        # Fonts:
        self.title_font = ("Helvetica", 50, "bold")
        self.text_font = ("Helvetica", 20, "normal")
        self.input_font = ("Helvetica", 17, "normal")
        
        # title settings:
        self.title_pady = 40

        # text_label settings:
        self.text_label_pady = 10

        # text_entry settings:
        self.text_entry_width = 50
        self.text_entry_bd = 10
        self.text_entry_pady = 20

        # start_button settings:
        self.start_button_width = 8
        self.start_button_height = 2
        self.start_button_bd = 0
        self.start_button_pady = 20

        self.countdown = 3