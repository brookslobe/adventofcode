import re

# "stacks" lul
# python list can be stack with push() and pop()

# use input part 1 (stack data)
# set up stacks of char (put stacks inside list)

aisles = []

# types of lines
# 1. Crate (has square brackets, letters, whitespace)
# 2. Stack numbers (has numbers, whitespace)
# 3. Whitespace line
# 4. Instructions (has leters, numbers, whitespace)

input_lines = []

CRATES_FIRST_LINE_NUM = 1
aisles_line_num = -1
whitespace_line_num = -1
instructions_first_line_num = -1
last_line_num = -1

whitespace_line_found = False

# read in input file
with open("input.txt", "rt") as input:
    whitespace_line_found = False
    for line_num, line in enumerate(input):
        line = line.rstrip()
        # print(line)
        input_lines.append(line)
        last_line_num = line_num

        if (not whitespace_line_found):

            rex_match = re.search("^\s*$", line)
            if (rex_match != None):
                whitespace_line_found = True
                whitespace_line_num = line_num
                aisles_line_num = whitespace_line_num - 1
                instructions_first_line_num = whitespace_line_num + 1

# determine how many stacks
print(input_lines[aisles_line_num])
max_aisle = re.findall("\d", input_lines[aisles_line_num])[-1]
max_aisle = int(max_aisle)
print("max aisle: ", max_aisle)
for aisle_num in range(max_aisle):
    aisles.append([])

# 1 .. 5 .. 9 .. 13 (char position of first few aisle numbers)
# we know many characters apart the ABC chars will be from each other
def is_char_pos_an_aisle(char_idx, line):
    return (char_idx - 1) % 4 == 0

def is_str_blank_or_empty(str):
    return not str or str.isspace()

def is_char_blank_or_empty(char):
    return char == None or char == '' or char == ' '

line_idx_data = aisles_line_num - 1
while line_idx_data >= 0:
    ln = input_lines[line_idx_data]
    print(ln)
    for char_idx, char in enumerate(ln):
        if(is_char_pos_an_aisle(char_idx, ln) and not is_char_blank_or_empty(char)):
            # print('is aisle')
            # print("ln: ", ln)
            # print("char idx: ", char_idx)
            # print("ln char index: ", ln[char_idx])
            aisles[(char_idx - 1) // 4].append(ln[char_idx])
        # else:
            # print('not aisle')
    line_idx_data -= 1

def print_aisles():
    for aisle in aisles:
        print(aisle)

print("~~~~~~~~~~~~~~~~~")
print_aisles()
print("~~~~~~~~~~~~~~~~~")


# use input part 2 (move instructions)

# while loop on number of iter
# decrement stack id by one for zero indexed list

instructions_idx_data = instructions_first_line_num
while instructions_idx_data <= last_line_num:
    ln = input_lines[instructions_idx_data]
    print(ln)

    nums = [int(s) for s in re.findall("\d+", ln)] # make sure to grab multiple consecutive digits
    moves_todo = nums[0]
    origin_aisle = nums[1] - 1
    destination_aisle = nums[2] - 1

    for m in range(0, moves_todo): # stop arg in range is exclusive
        c = aisles[origin_aisle].pop()
        # print(c)
        aisles[destination_aisle].append(c)
        
    print("........")
    print_aisles()
    instructions_idx_data += 1

chars_on_top = ""
for aisle in aisles:
    top_char = aisle.pop()
    chars_on_top += top_char

print(chars_on_top)