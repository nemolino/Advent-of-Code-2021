def day01_b():
    count = 0
    with open('in.txt') as f:
        window = [int(f.readline()), int(f.readline()), int(f.readline())]
        s = sum(window)
        for line in f:
            window = [window[1], window[2], int(line)]
            s_temp = sum(window)
            if s_temp > s:
                count += 1
            s = s_temp
    return count

if __name__ == "__main__": print(day01_b())
