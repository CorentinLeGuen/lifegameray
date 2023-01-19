from pyray import *
from raylib import FLAG_WINDOW_UNDECORATED, FLAG_VSYNC_HINT, MOUSE_BUTTON_LEFT

from grid import Grid

BORDER_GRAY = Color(162, 164, 166, 255)


class Application:
    def __init__(self):
        init_window(800, 900, "Life Game Ray")

        set_window_state(FLAG_WINDOW_UNDECORATED)
        set_window_state(FLAG_VSYNC_HINT)

        self.fps = 60
        self.frame = 0
        self.count = 0

        set_target_fps(60)

        self.grid_size = (10, 10)
        self.grid_ratio = (800 // self.grid_size[0], 800 // self.grid_size[1])
        self.grid = Grid(self.grid_size[0], self.grid_size[1])

        self.rect_debug = Rectangle(0, 800, 200, 50)
        self.text_debug = ("Debug on", "Debug off")
        self.measures_debug = (measure_text(self.text_debug[0], 15), measure_text(self.text_debug[1], 15))

        self.rect_quit = Rectangle(600, 800, 200, 100)
        self.text_quit = "Quit"
        self.measures_quit = measure_text(self.text_quit, 30)

        self.rect_play = Rectangle(200, 800, 200, 100)
        self.text_play = ("Run", "Stop")
        self.measures_play = (measure_text(self.text_play[0], 30), measure_text(self.text_play[1], 30))

        self.is_debug_enabled = True
        self.is_running = False

    def __run__(self):
        while not window_should_close():
            begin_drawing()
            clear_background(RAYWHITE)

            # Time clock ticker
            self.frame += 1
            if self.frame >= self.fps:
                self.count += 1
                self.frame = 0
                if self.is_running:
                    self.grid.tick()

            for row in range(self.grid_size[0]):
                for col in range(self.grid_size[1]):
                    if self.is_debug_enabled:
                        draw_rectangle_lines(self.grid_ratio[0] * row, self.grid_ratio[1] * col, self.grid_ratio[0], self.grid_ratio[1], LIGHTGRAY)
                    if self.grid.get_cell_at_position(row, col).is_alive:
                        draw_rectangle(self.grid_ratio[0] * row, self.grid_ratio[1] * col, self.grid_ratio[0], self.grid_ratio[1], BLACK)
                    elif self.is_debug_enabled:
                        draw_text(str(self.grid.get_cell_at_position(row, col).get_neighbors()), self.grid_ratio[0] * row + 10, self.grid_ratio[1] * col + 10, 18, LIGHTGRAY)

            # Draw background window
            draw_rectangle_lines(0, 0, 800, 800, DARKGRAY)
            draw_rectangle_lines(0, 799, 800, 101, DARKGRAY)

            # Draw buttons
            # # Debug
            draw_rectangle_rec(self.rect_debug, LIGHTGRAY)
            if self.is_debug_enabled:
                draw_text(self.text_debug[0], int(self.rect_debug.x + (self.rect_debug.width - self.measures_debug[0]) // 2), int(self.rect_debug.y + 10), 15, DARKGRAY)
            else:
                draw_text(self.text_debug[1], int(self.rect_debug.x + (self.rect_debug.width - self.measures_debug[1]) // 2), int(self.rect_debug.y + 10), 15, DARKGRAY)
            if check_collision_point_rec(get_mouse_position(), self.rect_debug) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                self.is_debug_enabled = not self.is_debug_enabled
            draw_rectangle_lines_ex(self.rect_debug, 1.0, BORDER_GRAY)

            if is_mouse_button_pressed(MOUSE_BUTTON_LEFT) and not self.is_running:
                mp = get_mouse_position()
                x = int(mp.x // self.grid_ratio[0])
                y = int(mp.y // self.grid_ratio[1])
                self.grid.switch_at_position(x, y)

            # # Play
            draw_rectangle_rec(self.rect_play, LIGHTGRAY)
            if self.is_running:
                draw_text(self.text_play[1], int(self.rect_play.x + (self.rect_play.width - self.measures_play[1]) // 2), int(self.rect_play.y + 30), 30, DARKPURPLE)
            else:
                draw_text(self.text_play[0], int(self.rect_play.x + (self.rect_play.width - self.measures_play[0]) // 2), int(self.rect_play.y + 30), 30, DARKGREEN)
            if check_collision_point_rec(get_mouse_position(), self.rect_play) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                self.is_running = not self.is_running
                self.frame = 0
            draw_rectangle_lines_ex(self.rect_play, 1.0, BORDER_GRAY)

            # # Quit
            draw_rectangle_rec(self.rect_quit, LIGHTGRAY)
            draw_text(self.text_quit, int(self.rect_quit.x + (self.rect_quit.width - self.measures_quit) // 2), int(self.rect_quit.y + 30), 30, DARKGRAY)
            draw_rectangle_lines_ex(self.rect_quit, 1.0, BORDER_GRAY)
            if check_collision_point_rec(get_mouse_position(), self.rect_quit) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                break

            end_drawing()


if __name__ == '__main__':
    app = Application()
    app.__run__()
    close_window()
