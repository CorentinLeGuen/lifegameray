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

        self.grid_size = (20, 20)
        self.grid_ratio = (800 // self.grid_size[0], 800 // self.grid_size[1])
        self.grid = Grid(self.grid_size[0], self.grid_size[1])

        self.rect_debug = Rectangle(0, 800, 200, 50)
        self.text_debug = ("Debug on", "Debug off")
        self.measures_debug = (measure_text(self.text_debug[0], 15), measure_text(self.text_debug[1], 15))

        self.rect_clean = Rectangle(600, 800, 200, 50)
        self.text_clean = "Clean up"
        self.measures_clean = measure_text(self.text_clean, 15)

        self.rect_quit = Rectangle(600, 850, 200, 50)
        self.text_quit = "Quit"
        self.measures_quit = measure_text(self.text_quit, 30)

        self.rect_play = Rectangle(200, 800, 200, 100)
        self.text_play = ("Run", "Stop")
        self.measures_play = (measure_text(self.text_play[0], 30), measure_text(self.text_play[1], 30))

        self.rect_speed = (Rectangle(400, 800, 50, 50), Rectangle(450, 800, 50, 50), Rectangle(500, 800, 50, 50), Rectangle(550, 800, 50, 50))
        self.text_speed = ("Speed", "-", "<speed>", "+")
        self.speeds = [1, 10, 15, 30, 45, 60]

        self.rect_grid = (Rectangle(400, 850, 50, 50), Rectangle(450, 850, 50, 50), Rectangle(500, 850, 50, 50), Rectangle(550, 850, 50, 50))
        self.text_grid = ("S", "M", "L", "XL")
        self.size_grid = (20, 50, 80, 100)

        self.text_credit = "Made by\nCorentin Le Guen"
        self.measures_credit = measure_text(self.text_credit, 15)

        self.speed = 3

        self.is_debug_enabled = True
        self.is_running = False

    def __run__(self):
        while not window_should_close():
            begin_drawing()
            clear_background(RAYWHITE)

            # Time clock ticker
            self.frame += 1
            if self.frame >= self.fps // self.speeds[self.speed]:
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

            draw_text(self.text_credit, int((200 - self.measures_credit) // 2), int(850 + 5), 15, DARKGRAY)

            # # Clean
            draw_rectangle_rec(self.rect_clean, LIGHTGRAY)
            draw_text(self.text_clean, int(self.rect_clean.x + (self.rect_clean.width - self.measures_clean) // 2), int(self.rect_clean.y + 10), 15, DARKGRAY)
            if check_collision_point_rec(get_mouse_position(), self.rect_clean) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                self.grid.clear()
                self.is_running = False
            draw_rectangle_lines_ex(self.rect_clean, 1.0, BORDER_GRAY)

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

            # # Speed
            draw_rectangle_rec(self.rect_speed[0], LIGHTGRAY)
            draw_rectangle_rec(self.rect_speed[1], LIGHTGRAY)
            draw_rectangle_rec(self.rect_speed[2], LIGHTGRAY)
            draw_rectangle_rec(self.rect_speed[3], LIGHTGRAY)

            draw_text(self.text_speed[0], int(self.rect_speed[0].x + 3), int(self.rect_speed[0].y + 15), 15, DARKGRAY)
            draw_text(self.text_speed[1], int(self.rect_speed[1].x + 15), int(self.rect_speed[1].y + 5), 45, DARKGRAY)
            draw_text(str(self.speeds[self.speed]), int(self.rect_speed[2].x + 10), int(self.rect_speed[2].y + 12), 30, DARKGRAY)
            draw_text(self.text_speed[3], int(self.rect_speed[3].x + 15), int(self.rect_speed[3].y + 5), 45, DARKGRAY)

            if check_collision_point_rec(get_mouse_position(), self.rect_speed[1]) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT) and self.speed > 0:
                self.speed -= 1
            elif check_collision_point_rec(get_mouse_position(), self.rect_speed[3]) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT) and self.speed < len(self.speeds) - 1:
                self.speed += 1

            draw_rectangle_lines_ex(self.rect_speed[1], 1.0, BORDER_GRAY)
            draw_rectangle_lines_ex(self.rect_speed[3], 1.0, BORDER_GRAY)

            # # Grid
            draw_rectangle_rec(self.rect_grid[0], LIGHTGRAY)
            draw_rectangle_rec(self.rect_grid[1], LIGHTGRAY)
            draw_rectangle_rec(self.rect_grid[2], LIGHTGRAY)
            draw_rectangle_rec(self.rect_grid[3], LIGHTGRAY)

            draw_text(self.text_grid[0], int(self.rect_grid[0].x + 10), int(self.rect_grid[0].y + 10), 30, DARKGRAY)
            draw_text(self.text_grid[1], int(self.rect_grid[1].x + 10), int(self.rect_grid[1].y + 10), 30, DARKGRAY)
            draw_text(self.text_grid[2], int(self.rect_grid[2].x + 10), int(self.rect_grid[2].y + 10), 30, DARKGRAY)
            draw_text(self.text_grid[3], int(self.rect_grid[3].x + 10), int(self.rect_grid[3].y + 10), 30, DARKGRAY)

            if check_collision_point_rec(get_mouse_position(), self.rect_grid[0]) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                self.__set_grid__(self.size_grid[0])
                self.is_running = False
            if check_collision_point_rec(get_mouse_position(), self.rect_grid[1]) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                self.__set_grid__(self.size_grid[1])
                self.is_running = False
            if check_collision_point_rec(get_mouse_position(), self.rect_grid[2]) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                self.__set_grid__(self.size_grid[2])
                self.is_running = False
            if check_collision_point_rec(get_mouse_position(), self.rect_grid[3]) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                self.__set_grid__(self.size_grid[3])
                self.is_running = False

            draw_rectangle_lines_ex(self.rect_grid[0], 1.0, BORDER_GRAY)
            draw_rectangle_lines_ex(self.rect_grid[1], 1.0, BORDER_GRAY)
            draw_rectangle_lines_ex(self.rect_grid[2], 1.0, BORDER_GRAY)
            draw_rectangle_lines_ex(self.rect_grid[3], 1.0, BORDER_GRAY)

            # # Quit
            draw_rectangle_rec(self.rect_quit, LIGHTGRAY)
            draw_text(self.text_quit, int(self.rect_quit.x + (self.rect_quit.width - self.measures_quit) // 2), int(self.rect_quit.y + 10), 30, DARKGRAY)
            draw_rectangle_lines_ex(self.rect_quit, 1.0, BORDER_GRAY)
            if check_collision_point_rec(get_mouse_position(), self.rect_quit) and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                break

            end_drawing()

    def __set_grid__(self, x: int):
        self.grid_size = (x, x)
        self.grid_ratio = (800 // self.grid_size[0], 800 // self.grid_size[1])
        self.grid = Grid(self.grid_size[0], self.grid_size[1])


if __name__ == '__main__':
    app = Application()
    app.__run__()
    close_window()
