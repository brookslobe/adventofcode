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

for line in input:
    line = line.rstrip()
    print(".....")
    print(line)
    line_len = len(line)
    half_line_len = line_len//2

    left = line[:half_line_len]
    right = line[half_line_len:]

    print(left)
    print(right)

    left_chars = {}
    for c in left:
        left_chars[c] = True

    common_char = ''
    for c in right:
        if (left_chars.get(c, False)):
            common_char = c
            break
  
    prio = priority_vals[common_char]

    print(common_char)
    print(prio)

    tot_prio += prio

print(tot_prio)

