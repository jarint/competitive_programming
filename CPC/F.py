import sys

dot = "."
pound = "#"
ErrMsg = "Error decoding image"

scanned_lines = []

while True:
    line = sys.stdin.readline().strip()
    if line:
        scanned_lines.append(line)
    else:
        break

def printer(line):
    global pound, dot
    
    if line[0] == "0":
        print(ErrMsg)
    
    if len(line) == 1:
        N = int(line[0])
        print()
        return

    parsed_line = []

    is_pound = False
    if line[0] == dot:
        is_pound = False
        line = line[1:]
    elif line[0] == pound:
        is_pound = True
        line = line[1:]
    
    for counter in line:
        this_count = int(counter)
        if is_pound:
            for i in range(this_count):
                parsed_line.append(pound)
                is_pound = not is_pound
        else:
            for i in range(this_count): 
                parsed_line.append(dot)
                is_pound = not is_pound
    
    print(''.join(parsed_line))
    
    
for line in scanned_lines:
    printer(line)