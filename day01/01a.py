def day01_a():
    count = 0
    with open('in.txt') as f:
        prev = int(f.readline())
        for line in f:
            nxt = int(line)
            if nxt > prev:
                count += 1
            prev = nxt
    return count

if __name__ == "__main__": print(day01_a())
