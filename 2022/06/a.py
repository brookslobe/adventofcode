SEQ_LEN = 4
recent_chars = []
last_char_of_marker = -1

with open("input.txt", "rt") as input:
    for line in input: # should only be one
        for char_idx, char in enumerate(line):
            recent_chars.append(char)
            
            if (len(recent_chars) > SEQ_LEN):
                recent_chars = recent_chars[1:] # remove first (oldest) element               

                charset = set()
                charset.update(recent_chars)
                if (len(charset) == SEQ_LEN):
                    sequence = "".join(str(s) for s in recent_chars)
                    last_char_of_marker = char_idx + 1
                    break

print(last_char_of_marker)