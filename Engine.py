

class Engine:
    def __init__(self, window_title="My Engine", width=500, height=500):
        self.window_title = window_title
        self.width = width
        self.height = height
        self.loop_state = False
        self.window = None
