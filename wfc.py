import random

class WFC:
    def __init__(self, width: int, height: int):
        self.resolution = self.width, self.height = width, height
        self.grid = [[[] for _ in range(self.width)] for _ in range(self.height)]
        self.rules = {}

    def set_mode(self, mode: str) -> None:
        if mode not in ["adjacency", "sockets"]:
            raise ValueError("Invalid Mode: {}".format(mode))
        self.mode = mode
        
    def assign_rules(self, element: str, rules: dict) -> None:
        self.rules[element] = rules

    def sockets_collapse(self, collapsing_y, collapsing_x):
        for k, socket in self.rules[self.grid[collapsing_y][collapsing_x]].items():
            relative_y = int(k.split(" ")[0])
            relative_x = int(k.split(" ")[1])

            x = relative_x + collapsing_x
            y = relative_y + collapsing_y

            if self.width <= x or x < 0 or self.height <= y or  y < 0 or type(self.grid[y][x]) != list:
                continue

            self.grid[y][x][:] = [element for element in self.grid[y][x] if self.rules[element][f"{-relative_y} {-relative_x}"] == socket]

    def adjacency_collapse(self, collapsing_y, collapsing_x):
        for element in self.rules[self.grid[collapsing_y][collapsing_x]]:
            
            # Determine cell above
            if collapsing_y-1 >= 0 and type(self.grid[collapsing_y-1][collapsing_x]) == list:
                self.grid[collapsing_y-1][collapsing_x][:] = [element for element in self.grid[collapsing_y-1][collapsing_x] if element in self.rules[self.grid[collapsing_y][collapsing_x]]]
                
            # Determine cell below
            if collapsing_y+1 < self.height and type(self.grid[collapsing_y+1][collapsing_x]) == list:
                self.grid[collapsing_y+1][collapsing_x][:] = [element for element in self.grid[collapsing_y+1][collapsing_x] if element in self.rules[self.grid[collapsing_y][collapsing_x]]]
                
            # Determine cell to the right
            if collapsing_x-1 >= 0 and type(self.grid[collapsing_y][collapsing_x-1]) == list:
                self.grid[collapsing_y][collapsing_x-1][:] = [element for element in self.grid[collapsing_y][collapsing_x-1] if element in self.rules[self.grid[collapsing_y][collapsing_x]]]
                
            # Determine cell to the left
            if collapsing_x+1 < self.width and type(self.grid[collapsing_y][collapsing_x+1]) == list:
                self.grid[collapsing_y][collapsing_x+1][:] = [element for element in self.grid[collapsing_y][collapsing_x+1] if element in self.rules[self.grid[collapsing_y][collapsing_x]]]

    def generate_grid(self):
        if not hasattr(self, 'mode'):
            raise ValueError("Rule book mod not set")
        
        # Assign every element to the grid
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                self.grid[y][x] = [element for element in self.rules]
        
        while True:
            
            # Get lowest entropy cell, or return if grid has been collapsed
            
            try:
                collapsing_y, collapsing_x = self.choose_lowest()
            except TypeError:
                break

            # Collapse cell
            self.grid[collapsing_y][collapsing_x] = random.choice(self.grid[collapsing_y][collapsing_x])

            match self.mode:
                case "sockets":
                    self.sockets_collapse(collapsing_y, collapsing_x)
                case "adjacency":
                    self.adjacency_collapse(collapsing_y, collapsing_x)
                case "balanced_adjacency":
                    raise ValueError("Mode {} not implemented".format(self.mode))
                    self.balanced_adjacency_collapse(collapsing_y, collapsing_x)
                case _:
                    raise ValueError("Mode {} not implemented".format(self.mode))

        return self.grid

    def choose_lowest(self):
        lowest = len(self.rules) + 1
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