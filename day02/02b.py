def day02_b():
    hpos, depth, aim = 0, 0, 0
    with open('in.txt') as f:
        for line in f:
            command, x = line.split()
            x = int(x)
            if command == 'down': aim += x
            elif command == 'up': aim -= x
            else:
                hpos += x
                depth += aim * x
    return hpos * depth

if __name__ == "__main__": print(day02_b())
