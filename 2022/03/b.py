import string

lower_abc = string.ascii_lowercase[:]
upper_abc = string.ascii_uppercase[:]

priority_vals = {}
LOWEST_PRIO = 1
ABC_LEN = len(lower_abc)

for idx, c in enumerate(lower_abc):
    priority_vals[c] = LOWEST_PRIO + idx
for idx, c in enumerate(upper_abc):
    priority_vals[c] = ABC_LEN + LOWEST_PRIO + idx

input = open("input.txt", "rt")
tot_prio = 0

print(lower_abc)
print(upper_abc)
print(priority_vals)

linenum = 0
prev_line = ""
prev_prev_line = ""

for line in input:
    line = line.rstrip()
    linenum += 1

    if (linenum % 3 == 0):
        print(".....")
        print(prev_prev_line)
        print(prev_line)
        print(line)

        cur_chars = {}
        prev_chars = {}
        prev_prev_chars = {}

        for c in line:
            cur_chars[c] = True
        for c in prev_line:
            prev_chars[c] = True
        for c in prev_prev_line:
            prev_prev_chars[c] = True

        common_chars = {x:cur_chars[x] for x in cur_chars if x in prev_chars}
        common_chars = {x:common_chars[x] for x in common_chars if x in prev_prev_chars}

        print(common_chars)
        if (len(common_chars.keys()) != 1):
            print("MORE THAN ONE REMAINING COMMON VALUE")
        common_char = next(iter(common_chars.keys())) # should only have one char
        print(common_char)
        prio = priority_vals[common_char]
        tot_prio += prio

    prev_prev_line = prev_line
    prev_line = line

print(tot_prio)