class Cell:
    def __init__(self):
        self.__alive = False
        self.__neighbors = 0

    def add_neighbor(self):
        self.__neighbors += 1

    def remove_neighbor(self):
        self.__neighbors -= 1

    def get_neighbors(self) -> int:
        return self.__neighbors

    def is_alive(self) -> bool:
        return self.__alive

    def switch_alive(self):
        self.__alive = not self.__alive


class Grid:
    def __init__(self, x: int, y: int):
        self.width = x
        self.height = y
        self.grid = [list([Cell() for _ in range(y)]) for _ in range(x)]

    def tick(self):
        new_grid = Grid(self.width, self.height)
        for x in range(self.width):
            for y in range(self.height):
                if (self.grid[x][y].get_neighbors() == 3 and not self.grid[x][y].is_alive()) \
                        or ((self.grid[x][y].get_neighbors() == 2 or self.grid[x][y].get_neighbors() == 3) and self.grid[x][y].is_alive()):
                    new_grid.switch_at_position(x, y)
        self.grid = new_grid.grid

    def clear(self):
        self.grid = [list([Cell() for _ in range(self.height)]) for _ in range(self.width)]

    def get_cell_at_position(self, x: int, y: int):
        return self.grid[x][y]

    def switch_at_position(self, x: int, y: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y].switch_alive()
            if self.grid[x][y].is_alive():
                if 0 <= x - 1:  # LEFT
                    self.grid[x - 1][y].add_neighbor()
                if 0 <= y - 1:  # UP
                    self.grid[x][y - 1].add_neighbor()
                    if 0 <= x - 1:  # UP / LEFT
                        self.grid[x - 1][y - 1].add_neighbor()
                    if x + 1 < self.width:  # UP / RIGHT
                        self.grid[x + 1][y - 1].add_neighbor()
                if x + 1 < self.width:  # RIGHT
                    self.grid[x + 1][y].add_neighbor()
                if y + 1 < self.height:  # DOWN
                    self.grid[x][y + 1].add_neighbor()
                    if 0 <= x - 1:  # LEFT
                        self.grid[x - 1][y + 1].add_neighbor()  # DOWN / LEFT
                    if x + 1 < self.width:  # RIGHT
                        self.grid[x + 1][y + 1].add_neighbor()  # DOWN / RIGHT
            else:
                if 0 <= x - 1:  # LEFT
                    self.grid[x - 1][y].remove_neighbor()
                if 0 <= y - 1:  # UP
                    self.grid[x][y - 1].remove_neighbor()
                    if 0 <= x - 1:  # UP / LEFT
                        self.grid[x - 1][y - 1].remove_neighbor()
                    if x + 1 < self.width:  # UP / RIGHT
                        self.grid[x + 1][y - 1].remove_neighbor()
                if x + 1 < self.width:  # RIGHT
                    self.grid[x + 1][y].remove_neighbor()
                if y + 1 < self.height:  # DOWN
                    self.grid[x][y + 1].remove_neighbor()
                    if 0 <= x - 1:  # LEFT
                        self.grid[x - 1][y + 1].remove_neighbor()  # DOWN / LEFT
                    if x + 1 < self.width:  # RIGHT
                        self.grid[x + 1][y + 1].remove_neighbor()  # DOWN / RIGHT
