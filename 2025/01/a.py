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

def spin_amount(line):
    line = line[1:]
    return int(line)

def trim_extra_spins(spin_amount):
    if (abs(spin_amount) >= 100):
        spin_amount = spin_amount % 100
    return spin_amount

def main():
    input = open("input.txt", "rt")

    global pos
    global pos_zero_hits

    for line in input:
        process_line(line)

    for line in lines:
        if (is_left(line)):
            pos -= spin_amount(line)
        else:
            pos += spin_amount(line)

        pos = trim_extra_spins(pos)

        if (pos < 0):
            pos += 100
        elif (pos >= 100):
            pos -= 100

        print(pos)

        if (pos == 0):
            pos_zero_hits += 1

    print("Final Position: ", pos)
    print("Position 0 Hits: ", pos_zero_hits)

if __name__ == "__main__":
    main()