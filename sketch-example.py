import sys
import ctypes
import sdl2.mouse
import Systems
from Engine import Engine


class Sketch(Engine):
    def __init__(self):
        Engine.__init__(self, window_title="My Sketch", width=600, height=600)

    def setup(self):
        pass

    def update(self):
        Systems.Render.clear_surface(self.get_surface())
        mx, my = ctypes.c_int(0), ctypes.c_int(0)
        sdl2.mouse.SDL_GetMouseState(ctypes.byref(mx), ctypes.byref(my))
        Systems.Render.line(self.get_surface(), 5, 5, mx.value, my.value, [128, 128, 128, 1])


if __name__ == '__main__':
    app = Sketch()
    sys.exit(app.run())
