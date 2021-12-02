def day02_a():
    hpos, depth = 0, 0
    with open('in.txt') as f:
        for line in f:
            command, x = line.split()
            x = int(x)
            if command == 'down': depth += x
            elif command == 'up': depth -= x
            else: hpos += x
    return hpos * depth

if __name__ == "__main__": print(day02_a())
