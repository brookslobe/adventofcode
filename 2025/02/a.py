import sys

def main(filename):
    input = open(filename, "rt") if filename else print("No filename provided")
    corpus = []
    print(type(corpus))
    for line in input:
        ranges = line.strip().split(',')
        corpus.extend(ranges)

    print(corpus)

    answer = solve(corpus)
    print("Answer:", answer)

def solve(input):

    id_consider = ""
    digit_count = 0

    invalid_ids = []
    all_invalid_ids = []

    for r in input:
        print(r)

        min = minFromRange(r)
        max = maxFromRange(r)
        invalid_ids = getInvalidIds(min, max)
        all_invalid_ids.extend(invalid_ids)
    
    print("Invalid IDs:", all_invalid_ids)

    answer = sum(all_invalid_ids)
    return answer

def getInvalidIds(min, max) -> list(int):
    invalid_ids = []
    minrange = int(min)
    maxrange = int(max)

    print("Checking range", minrange, "to", maxrange)

    for i in range(minrange, maxrange + 1):
        id = str(i)
        # print("Checking ID:", id)
        if not hasEvenDigitCount(id):
            continue
        
        max_pattern_len = len(id) // 2
        matching = True

        for char in range (0, max_pattern_len):
            front = id[0:char + 1]
            back = id[getHalfwayIdx(id): getHalfwayIdx(id) + char + 1]

            # print("Comparing front", front, "versus back", back)
            if front != back:
                matching = False
                continue

        if matching:
            invalid_ids.append(i)

        
    print("Invalid IDs in range", min, "to", max, ":", invalid_ids)
    return invalid_ids


def minFromRange(s):
    return s.split('-')[0]

def maxFromRange(s):
    return s.split('-')[1]

# "made only of some sequence of digits repeated twice"
def hasEvenDigitCount(s) -> bool:
    return (len(s) % 2) == 0

def getHalfwayIdx(s) -> int:
    return len(s) // 2

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        print("Include a file name like: python your_script.py <filename>")