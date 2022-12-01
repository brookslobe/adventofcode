# grab any fruit you see along the way

# one star per puzzle
# need 50 stars...aka solve all 25x2 puzzles

# some resources are limited
# Food (measured in Calories) as an example of a resource

# calories is puzzle input




# line delimited calorie counts
# empty line to delimit new elf


# RETURN: which elf has the most calories?
# ...probably need to keep track of each elf calories since you'd reshuffle or give to least

from functools import reduce

elves = []
input = open("input.txt", "rt")
new_elf = True
pointer = -1 # will get incremented to 0 on first go

for line in input:
    if (line == "" or line == "\n" or line == "\r"):
        new_elf = True
    elif (new_elf):
        elves.append(int(line))
        new_elf = False
        pointer += 1
    else:
        elves[pointer] += int(line)

max = reduce(lambda a,b: max(a,b), elves)
print(max)