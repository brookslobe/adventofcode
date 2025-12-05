import sys

MARKED_ACESSIBLE = 'x'

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
    accessible_rolls = 0

    grid = fillGrid(input)
    marked_grid = grid
    # printAsGrid(grid)

    directions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

    rows = len(grid)
    cols = len(grid[0])
    maxRow = rows-1
    maxCol = cols-1

    for row in range(rows):
        line = input[row]
        # could DFS as well but it's just an easy 2d rectangle
        for col in range(cols):
            c = input[row][col]
            
            grid[row][col] = c
            marked_grid[row][col] = c

            # could save previous results or "visited coordinate"

            if not isRoll(c):
                continue

            adjacent_rolls = 0
            for dx, dy in directions:
                if not isInBounds(maxRow, maxCol, row+dx, col+dy):
                    continue

                neighbor = grid[row+dx][col+dy]
                
                if isRoll(neighbor):
                    adjacent_rolls += 1

            if adjacent_rolls < 4:
                accessible_rolls += 1
                marked_grid[row][col] = MARKED_ACESSIBLE
    
    printAsGrid(marked_grid)

    return accessible_rolls

def printAsGrid(list_2d):
    for l in list_2d:
        print(str(l))

def isInBounds(maxRow, maxCol, row, col):
    return (0 <= row <= maxRow) and (0 <= col <= maxCol)

def isRoll(c):
    return c != '.'

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