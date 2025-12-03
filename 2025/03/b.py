import sys

BANK_LENGTH = 12

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
    battery_joltages = []

    for line in input:
        if len(line) < BANK_LENGTH:
            print("Line too short, skipping:", line)
            break

        batteries_active = line[0]
        batteries_remaining = line[1:]
        batteries_active = chooseBatteries(batteries_active, batteries_remaining)

        battery_joltages.append(int(batteries_active))

    print(battery_joltages)
    answer = sum(battery_joltages)
    return answer
    
def chooseBatteries(batteries_active, batteries_remaining):
    if mustUseRemainingChars(batteries_active, batteries_remaining):
        return batteries_active + batteries_remaining

    candidate = batteries_remaining[0]
    batteries_remaining = batteries_remaining[1:]
    
    if (batteries_active[-1] < candidate):
        batteries_active = batteries_active[:-1] + candidate
    elif (len(batteries_active) < BANK_LENGTH):
        batteries_active += candidate

    batteries_active = shaveExpendableDigits(batteries_active, batteries_remaining)
    return chooseBatteries(batteries_active, batteries_remaining)

def shaveExpendableDigits(s, batteries_remaining):

    if (len(s) < 2 or mustUseRemainingChars(s, batteries_remaining)):
        # couldn't shave any more based on remaining chars
        return s

    if s[-2] < s[-1]:
        s_trimmed = s[:-2] + s[-1] # shave off the second to last digit
        return shaveExpendableDigits(s_trimmed, batteries_remaining)
    else:
        return s

def mustUseRemainingChars(candidateChunk, lineRemaining):
    return BANK_LENGTH - len(candidateChunk) == len(lineRemaining)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        print("Include a file name like: python your_script.py <filename>")