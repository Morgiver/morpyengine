import sdl2
import sdl2.ext
from Constants import *


class Engine:
    def __init__(self, window_title="My Engine", width=500, height=500):
        self.window_title = window_title
        self.width = width
        self.height = height
        self.loop_state = LOOP_STATE_STOPPED
        self.window = None

    def set_loop_state(self, state):
        if state == LOOP_STATE_RUNNING or state == LOOP_STATE_STOPPED or state == LOOP_STATE_PAUSED:
            self.loop_state = state
