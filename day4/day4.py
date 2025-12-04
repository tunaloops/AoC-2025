with open("input.txt", "r", encoding="utf-8") as f:
    read_data=f.read().splitlines()

# proper way to split continuous string, split() defaults to whitespace
grid = [[char for char in data] for data in read_data]

def check_neighbors(arr, r, c):
    neighbor_rolls = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            else:
                nr = r + dr
                nc = c + dc
                # make sure the neighbors being checked are inside the grid
                if 0 <= nr < len(arr) and 0 <= nc < len(arr[nr]):
                    if arr[nr][nc] == "@":
                        neighbor_rolls += 1
                        if neighbor_rolls == 4:
                            return neighbor_rolls
    
    return neighbor_rolls

valid_rolls = 0
for row in range(len(grid)):      
    for col in range(len(grid[row])):     
        if grid[row][col] != "@":
            continue
        else:
            check = check_neighbors(grid, row, col)
            if check < 4:
                valid_rolls += 1

print(valid_rolls)