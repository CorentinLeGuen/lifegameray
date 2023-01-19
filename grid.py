class Cell:
    def __init__(self):
        self.is_alive = False
        self.neighbors = 0

    def add_neighbor(self):
        self.neighbors += 1

    def remove_neighbor(self):
        self.neighbors -= 1

    def get_neighbors(self) -> int:
        return self.neighbors

    def is_alive(self) -> bool:
        return self.is_alive

    def switch_alive(self):
        self.is_alive = not self.is_alive

    def __repr__(self):
        if self.is_alive:
            return '(O, ' + str(self.get_neighbors()) + ')'
        return '(X, ' + str(self.get_neighbors()) + ')'


class Grid:
    def __init__(self, x: int, y: int):
        self.width = x
        self.height = y
        self.grid = [list([Cell() for _ in range(y)]) for _ in range(x)]

    def tick(self):
        # Apply 4 rules
        return self.height * [self.width * [Cell()]]

    def get_cell_at_position(self, x: int, y: int):
        return self.grid[x][y]

    def switch_at_position(self, x: int, y: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y].switch_alive()
            if self.grid[x][y].is_alive:
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

    def __str__(self):
        res = ''
        for x in self.grid:
            res += str(x) + ',\n'
        return res
