def does_engulf(assign1, assign2):
    if (assign1[0] <= assign2[0] and assign1[1] >= assign2[1]) :
        return True # assign1 engulfs
    elif (assign1[0] >= assign2[0] and assign1[1] <= assign2[1]) :
        return True # assign2 engulfs
    else:
        return False

cnt_pairs_engulf = 0

# 14-38,14-14
# 2-10,3-55
# 36-90,36-46
input = open("input.txt", "rt")

for line in input:
    line = line.rstrip()
    print(".....")
    print(line)

    halves = line.split(',')
    half1 = halves[0].split('-')
    half2 = halves[1].split('-')

    half1first = half1[0]
    half1second = half1[1]

    half1first = int(half1first)
    half1second = int(half1second)

    assign1 = (half1first, half1second)

    half2first = half2[0]
    half2second = half2[1]

    half2first = int(half2first)
    half2second = int(half2second)
    
    assign2 = (half2first, half2second)

    if (does_engulf(assign1, assign2)):
        cnt_pairs_engulf += 1

print(cnt_pairs_engulf)