import sys

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
        if len(line) < 2: # battery must have 2+ digits
            continue 

        # print(line, "<- line")

        maxDigitAtEnd = False

        maxDigit = getMaxDigit(line)

        followupBatteryChunk = ""

        batteryWithoutFinalDigit = line[0 : (len(line) -1)]
        if not (str(maxDigit)) in batteryWithoutFinalDigit:
            maxDigitAtEnd = True
            followupBatteryChunk = batteryWithoutFinalDigit
        else:
            firstMatchIdx = line.index(str(maxDigit))
            followupBatteryChunk = line[firstMatchIdx + 1 : len(line)]

        # print(followupBatteryChunk, "<- followup chunk")

        maxDigit2 = getMaxDigit(followupBatteryChunk)
        batteryJoltage = str(maxDigit) + str(maxDigit2) if not maxDigitAtEnd else str(maxDigit2) + str(maxDigit)

        battery_joltages.append(int(batteryJoltage))      
    
    print(battery_joltages)

    answer = sum(battery_joltages)
    return answer

def getMaxDigit(line):
    digitSet = strAsIntSet(line)
    maxDigit = maxFromSet(digitSet)
    return maxDigit

def firstCharOccurence(s, char):
    for idx in range(len(s)):
        if s[idx] == char:
            return idx
    return -1

def maxFromSet(intSet):
    maxVal = -1
    for val in intSet:
        if val > maxVal:
            maxVal = val
    return maxVal

def strAsIntSet(s):
    return set(int(char) for char in s)

def isLastChar(s, idx):
    return idx == len(s) - 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        print("Include a file name like: python your_script.py <filename>")