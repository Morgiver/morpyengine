import sdl2
import sdl2.ext


class Render:
    @staticmethod
    def line(surface, x1, y1, x2, y2, color):
        color = sdl2.ext.Color(color[0], color[1], color[2], color[3])
        sdl2.ext.line(surface, color, (x1, y1, x2, y2))

    @staticmethod
    def rect(surface, x, y, w, h, color):
        color = sdl2.ext.Color(color[0], color[1], color[2], color[3])
        sdl2.ext.fill(surface, color, (x, y, w, h))

    @staticmethod
    def clear_surface(surface):
        sdl2.ext.fill(surface, 0)
