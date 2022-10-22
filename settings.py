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
        self.text_font = ("Helvetica", 18, "normal")
        self.input_font = ("Helvetica", 17, "normal")
        
        # title settings:
        self.title_pady = 40

        # text_label settings:
        self.text_label_pady = 10

        # text_entry settings:
        self.text_entry_width = 60
        self.text_entry_bd = 10
        self.text_entry_pady = 20

        # start_button settings:
        self.start_button_width = 8
        self.start_button_height = 2
        self.start_button_bd = 0
        self.start_button_pady = 20

        self.quotes = ("For the things we have to learn before we can do them, we learn by doing them",
                  "Practice doesn't make perfect.Practice reduces the imperfection.",
                  "A photograph shouldn't be just a picture, it should be a philosophy.",
                  "You need mountains, long staircases don't make good hikers.",
                  "An ounce of practice is generally worth more than a ton of theory.",
                  "You don’t know anything, but I know even less.",
                  "No matter how gloomy the morning, it is a new day where anything is possible.",
                  "I accept no responsibility for anything I did while drunk.",
                  "The SOME of something is not the SUM of something...",
                  "I'm not a great programmer; I'm just a good programmer with great habits.",
                  "The only way to go fast, is to go well.",
                  'if you can write "hello world" you can change the world',
                  "Happiness should be a function without any parameters.")

        self.countdown = 3