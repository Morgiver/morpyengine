import sys
import Systems
from Engine import Engine


class Sketch(Engine):
    def __init__(self):
        Engine.__init__(self, window_title="My Sketch", width=600, height=600)

    def setup(self):
        pass

    def update(self):
        Systems.Render.clear_surface(self.get_surface())
        mx, my = self.get_mouse_state()
        Systems.Render.line(self.get_surface(), 5, 5, mx, my, [128, 128, 128, 1])


if __name__ == '__main__':
    app = Sketch()
    sys.exit(app.run())
