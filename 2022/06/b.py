START_PACKET_SEQ_LEN = 4
START_MSG_SEQ_LEN = 14
recent_chars = []
last_char_of_marker = -1

with open("input.txt", "rt") as input:
    for line in input: # should only be one
        for char_idx, char in enumerate(line):
            recent_chars.append(char)
            
            if (len(recent_chars) > START_MSG_SEQ_LEN):
                recent_chars = recent_chars[1:] # remove first (oldest) element               

                charset = set()
                charset.update(recent_chars)
                # looks like unique14 for message can share with unique4 of packet
                if (len(charset) == START_MSG_SEQ_LEN):
                    sequence = "".join(str(s) for s in recent_chars)
                    last_char_of_marker = char_idx + 1
                    break

print(last_char_of_marker)