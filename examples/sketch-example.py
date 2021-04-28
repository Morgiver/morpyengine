import sys
from src.morpyengine.Engine import Engine
from src.morpyengine.Systems import Render, Mouse


class Sketch(Engine):
    def __init__(self):
        Engine.__init__(self, window_title="My Sketch", width=600, height=600)

    def setup(self):
        pass

    def update(self):
        Render.clear_surface(self.get_surface())
        mx, my = Mouse.get_mouse_position()
        Render.line(self.get_surface(), 5, 5, mx, my, [128, 128, 128, 1])


if __name__ == '__main__':
    app = Sketch()
    sys.exit(app.run())
