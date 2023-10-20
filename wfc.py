import random

random.seed(1)
RESOLUTION = COLUMNS, ROWS = 10, 10

grid = [[[] for _ in range(ROWS)] for _ in range(COLUMNS)]

rule_sockets = {
    "blank": {
        "0 1": 0,
        "1 0": 0,
        "0 -1": 0,
        "-1 0": 0
    },
    
    "top": {
        "0 1": 1,
        "1 0": 1,
        "0 -1": 0,
        "-1 0": 1
    },
    
    "left": {
        "0 1": 1,
        "1 0": 0,
        "0 -1": 1,
        "-1 0": 1
    },
    
    "bot": {
        "0 1": 0,
        "1 0": 1,
        "0 -1": 1,
        "-1 0": 1
    },
    
    "right": {
        "0 1": 1,
        "1 0": 1,
        "0 -1": 1,
        "-1 0": 0
    }
}

for x, col in enumerate(grid):
    for y, i in enumerate(col):
        grid[x][y] = ["blank", "top", "right", "bot", "left"]

def choose_lowest(grid):
    lowest = 6
    coors = []
    
    # Find lowest probability
    
    for x, col in enumerate(grid):
        for y, i in enumerate(col):
            if type(i) != list:
                continue
            
            if len(i) < 1:
                raise ValueError(f"Element ({x}, {y}) reached 0 possible states")
            
            if lowest > len(i):
                coors = []
                coors.append((x, y))
                lowest = len(i)
            elif lowest == len(i):
                coors.append((x, y))
    
    # choose a random out of the lowest ones
    
    if coors == []:
        return None
    
    return random.choice(coors)

while True:
    # collapse random cell with lowest chances
    try:
        collapsing_x, collapsing_y = choose_lowest(grid)
    except:
        break
    
    grid[collapsing_x][collapsing_y] = random.choice(grid[collapsing_x][collapsing_y])
    
    # compute new wave function for other neighboring cells
    for k, socket in rule_sockets[grid[collapsing_x][collapsing_y]].items():
        relative_x = int(k.split(" ")[0])
        relative_y = int(k.split(" ")[1])
        
        # get new coordinates
        x = relative_x + collapsing_x
        y = relative_y + collapsing_y
        
        # check if neighbor cell is outside grid or is already collapsed
        if COLUMNS <= x or x < 0 or ROWS <= y or y < 0 or type(grid[x][y]) != list:
            continue
        
        # remove conflicting elements
        grid[x][y][:] = [element for element in grid[x][y] if rule_sockets[element][f"{-relative_x} {-relative_y}"] == socket]

for col in grid:
    print(*col, sep="\t")
