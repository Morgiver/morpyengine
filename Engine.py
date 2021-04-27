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

    def setup(self):
        pass

    def update(self):
        pass

    def set_loop_state(self, state):
        if state == LOOP_STATE_RUNNING or state == LOOP_STATE_STOPPED or state == LOOP_STATE_PAUSED:
            self.loop_state = state

    def handle_events(self, events):
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                self.set_loop_state(LOOP_STATE_STOPPED)
                break

    def get_surface(self):
        return self.window.get_surface()
