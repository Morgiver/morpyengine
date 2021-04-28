import sdl2
import sdl2.ext
import sdl2.mouse
import ctypes


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


class Mouse:
    @staticmethod
    def get_mouse_position():
        mx, my = ctypes.c_int(0), ctypes.c_int(0)
        sdl2.mouse.SDL_GetMouseState(ctypes.byref(mx), ctypes.byref(my))
        return mx.value, my.value
