loss_pts = 0
tie_pts = 3
win_pts = 6

min_idx = 0
max_idx = 2

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
you_idx_to_move = {
    0: "X",
    1: "Y",
    2: "Z"
}

your_move_choice_pts = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

outcome_pts = {
    "X": 0,
    "Y": 3,
    "Z": 6
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

def determine_you_move_idx(them, outcome):
    if (outcome == "X"): # lose
        return max_idx if (them_move_idx[them] == min_idx) else them_move_idx[them] - 1
    elif (outcome == "Y"): # tie
        return them_move_idx[them]
    else: # win
        return min_idx if (them_move_idx[them] == max_idx) else them_move_idx[them] + 1


tot_score = 0

input = open("input.txt", "rt")

for line in input:
    line = line.rstrip() # remove trailing whitespace to avoid printing newlines
    print(line)
    their_move = line[0]
    outcome = line[2]

    rd_score = outcome_pts[outcome] + your_move_choice_pts[you_idx_to_move[determine_you_move_idx(their_move, outcome)]]

    print("... ", rd_score)
    tot_score += rd_score

print(tot_score)