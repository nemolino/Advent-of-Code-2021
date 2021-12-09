from functools import reduce

with open('in.txt') as f:
    lines = [[int(el) for el in line.strip()] for line in f.readlines()]
    num_of_lines = len(lines)
    line_len = len(lines[0])

def day09_a():

    res = 0
    
    for i in range(num_of_lines):
        for j in range(line_len):    
            if not ( (i == 0 or lines[i][j] < lines[i-1][j]) and (i == num_of_lines - 1 or lines[i][j] < lines[i+1][j]) ): continue
            if not ( (j == 0 or lines[i][j] < lines[i][j-1]) and (j == line_len-1 or lines[i][j] < lines[i][j+1]) ): continue
            res += lines[i][j] + 1

    return res
    
def basin_size(i, j):

    t = []
    size = 0

    def basin_size_recursive(i, j):
        t.append((i,j))
        nonlocal size
        size += 1
        if j != 0               and lines[i][j-1] != 9 and not (i,j-1) in t:   basin_size_recursive(i, j-1)
        if j != line_len-1      and lines[i][j+1] != 9 and not (i,j+1) in t:   basin_size_recursive(i, j+1)
        if i != num_of_lines-1  and lines[i+1][j] != 9 and not (i+1,j) in t:   basin_size_recursive(i+1, j)
        if i != 0               and lines[i-1][j] != 9 and not (i-1,j) in t:   basin_size_recursive(i-1, j)
        return

    basin_size_recursive(i, j)
    return size
    
def day09_b():

    basin_sizes = []
        
    for i in range(num_of_lines):
        for j in range(line_len):
            if not ( (i == 0 or lines[i][j] < lines[i-1][j]) and (i == num_of_lines - 1 or lines[i][j] < lines[i+1][j]) ): continue
            if not ( (j == 0 or lines[i][j] < lines[i][j-1]) and (j == line_len-1 or lines[i][j] < lines[i][j+1]) ): continue
            basin_sizes.append(basin_size(i, j))

    return reduce((lambda x, y: x * y), sorted(basin_sizes)[-3:])

if __name__ == "__main__":
    print(day09_a())
    print(day09_b())
