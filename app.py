from pyray import *
from raylib import FLAG_WINDOW_UNDECORATED, FLAG_VSYNC_HINT, KEY_DOWN, KEY_UP, KEY_ENTER, KEY_LEFT, KEY_RIGHT


class Application:
    def __init__(self):
        init_window(800, 900, "Life Game Ray")

        set_window_state(FLAG_WINDOW_UNDECORATED)
        set_window_state(FLAG_VSYNC_HINT)
        set_target_fps(60)

    def __run__(self):
        while not window_should_close():
            begin_drawing()
            clear_background(RAYWHITE)

            draw_rectangle_lines(0, 0, 800, 800, DARKGRAY)
            draw_rectangle_lines(0, 799, 800, 101, DARKGRAY)

            end_drawing()


if __name__ == '__main__':
    app = Application()
    app.__run__()
    close_window()
