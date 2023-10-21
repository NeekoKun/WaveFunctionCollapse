from wfc import WFC

wfc = WFC(3, 3, seed = 0)

wfc.assign_rules("blank", {"0 1": 0, "1 0": 0, "0 -1": 0, "-1 0": 0})
wfc.assign_rules("top",   {"0 1": 1, "1 0": 0, "0 -1": 1, "-1 0": 1})
wfc.assign_rules("right", {"0 1": 1, "1 0": 1, "0 -1": 0, "-1 0": 1})
wfc.assign_rules("bot",   {"0 1": 1, "1 0": 1, "0 -1": 1, "-1 0": 0})
wfc.assign_rules("left",  {"0 1": 0, "1 0": 1, "0 -1": 1, "-1 0": 1})

grid = wfc.generate_grid()

for row in grid:
    print(*row, sep="\t")