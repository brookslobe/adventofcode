import sys

START_POS = 50
lines = []
pos_zero_hits = 0
pos = START_POS

def process_line(line):
    l = line.strip()
    lines.append(l)

def is_left(line):
    if (line[0] == "L"):
        return True
    return False

def get_spin_amount(line):
    line = line[1:]
    return int(line)

def trim_extra_spins(spin_amount):
    return spin_amount % 100

def count_extra_spins(spin_amount):
    return spin_amount // 100

prev_touches = 0
def did_touches_increase(touches):
    return touches > prev_touches
            
def main(filename):
    input = open(filename, "rt") if filename else print("No filename provided")

    global pos
    global pos_zero_hits

    for line in input:
        process_line(line)

    print(f"Starting Position: {pos}")

    for line in lines:

        spin_amount = get_spin_amount(line)
        pos_zero_hits += count_extra_spins(spin_amount)
        pos_change = trim_extra_spins(spin_amount)

        if (is_left(line)):
            intersect = pos % 100
        else:
            intersect = (100 - pos) % 100

        if (intersect == 0):
            intersect = 100

        if (intersect <= pos_change):
            pos_zero_hits += 1 + ((pos_change - intersect) // 100)

        if (is_left(line)):
            pos = (pos - spin_amount) % 100
        else:
            pos = (pos + spin_amount) % 100

    print("Final Position: ", pos)
    print("Times touched zero: ", pos_zero_hits)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        print("Include a file name like: python your_script.py <filename>")