from pyray import *
from raylib import FLAG_WINDOW_UNDECORATED, FLAG_VSYNC_HINT, KEY_DOWN, KEY_UP, KEY_ENTER, KEY_LEFT, KEY_RIGHT, MOUSE_BUTTON_LEFT

from grid import Grid


class Application:
    def __init__(self):
        init_window(800, 900, "Life Game Ray")

        set_window_state(FLAG_WINDOW_UNDECORATED)
        set_window_state(FLAG_VSYNC_HINT)
        set_target_fps(60)

        self.grid_size = (10, 10)
        self.grid_ratio = (800 // self.grid_size[0], 800 // self.grid_size[1])
        self.grid = Grid(self.grid_size[0], self.grid_size[1])

    def __run__(self):
        while not window_should_close():
            begin_drawing()
            clear_background(RAYWHITE)

            for row in range(self.grid_size[0]):
                for col in range(self.grid_size[1]):
                    draw_rectangle_lines(self.grid_ratio[0] * row, self.grid_ratio[1] * col, self.grid_ratio[0], self.grid_ratio[1], LIGHTGRAY)
                    if self.grid.get_cell_at_position(row, col).is_alive:
                        draw_rectangle(self.grid_ratio[0] * row, self.grid_ratio[1] * col, self.grid_ratio[0], self.grid_ratio[1], BLACK)
                    else:
                        draw_text(str(self.grid.get_cell_at_position(row, col).get_neighbors()), self.grid_ratio[0] * row + 10, self.grid_ratio[1] * col + 10, 18, LIGHTGRAY)

            draw_rectangle_lines(0, 0, 800, 800, DARKGRAY)
            draw_rectangle_lines(0, 799, 800, 101, DARKGRAY)

            if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                mp = get_mouse_position()
                x = int(mp.x // self.grid_ratio[0])
                y = int(mp.y // self.grid_ratio[1])
                self.grid.switch_at_position(x, y)

            end_drawing()


if __name__ == '__main__':
    app = Application()
    app.__run__()
    close_window()
