import sdl2
import sdl2.ext


class Render:
    def line(self, surface, x1, y1, x2, y2, color):
        color = sdl2.ext.Color(color[0], color[1], color[2], color[3])
        sdl2.ext.line(surface, color, (x1, y1, x2, y2))

    def rect(self, surface, x, y, w, h, color):
        color = sdl2.ext.Color(color[0], color[1], color[2], color[3])
        sdl2.ext.fill(surface, color, (x, y, w, h))

    def clear_surface(self, surface):
        sdl2.ext.fill(surface, 0)
