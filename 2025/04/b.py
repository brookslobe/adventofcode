import sys

MARKED_EMPTY = '.'

def main(filename):
    if not filename:
        print("No filename provided")
        return

    with open(filename, "rt") as input:
        corpus = []
        for line in input:
            corpus.append(line.strip())

    answer = solve(corpus)
    print("Answer:", answer)

def solve(input):
    rolls_removed = 0

    grid = fillGrid(input)
    # printAsGrid(grid)

    directions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

    rows = len(grid)
    cols = len(grid[0])
    maxRow = rows-1
    maxCol = cols-1

    visited = set()
    stack = []
    stack.append((0, 0))
    visited.add((0, 0))

    while stack:
        row, col = stack.pop()
        # print(f"visiting cell ({row}, {col}) with value {grid[row][col]}")

        adjacent_rolls = []
        for dx, dy in directions:
            if not isInBounds(maxRow, maxCol, row+dx, col+dy):
                continue

            if not (row+dx, col+dy) in visited:
                stack.append((row+dx, col+dy)) # discover unvisited neighbors in grid
                visited.add((row+dx, col+dy))

            if isRoll(grid[row][col]):
                neighbor = grid[row+dx][col+dy]
                
                if isRoll(neighbor):
                    adjacent_rolls.append((row+dx, col+dy))

        if isRoll(grid[row][col]) and len(adjacent_rolls) < 4: # shouldn't check here and inside dx,dy loop both
            rolls_removed += 1
            grid[row][col] = MARKED_EMPTY

            for x, y in adjacent_rolls:
                stack.append((x, y))
    
    # printAsGrid(grid)
    return rolls_removed

def printAsGrid(list_2d):
    for l in list_2d:
        print(l)

def isInBounds(maxRow, maxCol, row, col):
    return (0 <= row <= maxRow) and (0 <= col <= maxCol)

def isRoll(c):
    return c == '@'

def fillGrid(input):
    # assuming nonjagged grid
    row_cnt = len(input)
    col_cnt = len(input[0])

    grid = [['' for _ in range(col_cnt)] for _ in range(row_cnt)]

    for row in range(col_cnt):
        line = input[row]
        for col in range(row_cnt):
            c = input[row][col]
            
            grid[row][col] = c

    return grid

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        print("Include a file name like: python your_script.py <filename>")