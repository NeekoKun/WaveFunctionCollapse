import random

class WFC:
    def __init__(self, width: int, height: int, seed = None):
        self.resolution = self.width, self.height = width, height
        self.grid = [[[] for _ in range(self.width)] for _ in range(self.height)]
        self.rule_sockets = {}

        if seed:
            random.seed = seed

    def assign_rules(self, name: str, sockets: dict) -> None:
        self.rule_sockets[name] = sockets

    def generate_grid(self):
        # Assign everry element to the grid
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                self.grid[y][x] = [element for element in self.rule_sockets]
        
        while True:
            try:
                collapsing_y, collapsing_x = self.choose_lowest()
            except:
                break

            self.grid[collapsing_y][collapsing_x] = random.choice(self.grid[collapsing_y][collapsing_x])

            for k, socket in self.rule_sockets[self.grid[collapsing_y][collapsing_x]].items():
                relative_y = int(k.split(" ")[0])
                relative_x = int(k.split(" ")[1])

                x = relative_x + collapsing_x
                y = relative_y + collapsing_y

                if self.width <= x or x < 0 or self.height <= y or  y < 0 or type(self.grid[y][x]) != list:
                    continue

                self.grid[y][x][:] = [element for element in self.grid[y][x] if self.rule_sockets[element][f"{-relative_y} {-relative_x}"] == socket]

        return self.grid

    def choose_lowest(self):
        lowest = len(self.rule_sockets) + 1
        coors = []

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if type(cell) != list:
                    continue

                if len(cell) < 1:
                    raise ValueError
                
                if lowest > len(cell):
                    coors = []
                    coors.append((y, x))
                    lowest = len(cell)
                elif lowest == len(cell):
                    coors.append((y, x))
        if coors == []:
            return None
        
        return random.choice(coors)