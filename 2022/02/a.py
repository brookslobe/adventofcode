loss_pts = 0
tie_pts = 3
win_pts = 6

them_move_idx = {
    "A": 0,
    "B": 1,
    "C": 2
}

you_move_idx = {
    "X": 0,
    "Y": 1,
    "Z": 2
}

your_move_choice_pts = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def round_score(them, you):
    them_idx = them_move_idx[them]
    you_idx = you_move_idx[you]

    if (you_idx + 1 == them_idx or (them_idx == 0 and you_idx == 2)):
        return loss_pts + your_move_choice_pts[you]
    elif (you_idx == them_idx):
        return tie_pts + your_move_choice_pts[you]
    else:
        return win_pts + your_move_choice_pts[you]


tot_score = 0

input = open("input.txt", "rt")

for line in input:
    line = line.rstrip() # remove trailing whitespace to avoid printing newlines
    print(line)
    their_move = line[0]
    your_move = line[2]
    rd_score = round_score(their_move, your_move)
    print("... ", rd_score)
    tot_score += rd_score

print(tot_score)