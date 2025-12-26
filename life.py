import random

def make_grid(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]

def populate_grid_random(grid, density):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if random.random() < density:
                grid[y][x] = 1

def count_live_neighbor_cells(grid, x, y, grid_width, grid_height):
    count = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_width and 0 <= ny < grid_height:
                count += grid[ny][nx]
    return count

def step(grid):
    height = len(grid)
    width = len(grid[0])
    new_grid = make_grid(width, height)

    for y in range(height):
        for x in range(width):
            n = count_live_neighbor_cells(grid, x, y, width, height)
            if grid[y][x] == 1 and n in (2, 3):
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and n == 3:
                new_grid[y][x] = 1

    return new_grid