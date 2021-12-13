def day13():
    
    res, coordinates, mat = [0, 0], [], []
    x_max, y_max = 0, 0
    
    with open('in.txt') as f:
        
        for line in f:
            if line != '\n':
                x, y = [int(el) for el in line.strip().split(',')]
                if x > x_max: x_max = x
                if y > y_max: y_max = y
                coordinates.append((x, y))
            else:
                break
            
        x_max += 1
        y_max += 1
        
        for y in range(0, y_max): mat.append(['.'] * (x_max))
        while len(coordinates) > 0:
            x, y = coordinates.pop(0)
            mat[y][x] = '#'
    
        for line in f:

            folding_axes, folding_along = [el for el in line.strip().split('=')]
            folding_along = int(folding_along)
            
            if folding_axes[-1] == 'x':
                
                for y in range(0, y_max):
                    for x in range(folding_along+1, x_max):
                        if mat[y][2*folding_along - x] != '#': mat[y][2*folding_along - x] = mat[y][x]
                
                for y in range(0, y_max): mat[y] = mat[y][:folding_along] # removing folded columns

                x_max = folding_along

            else:

                for y in range(folding_along+1, y_max):
                    for x in range(0, x_max):
                        if mat[2*folding_along - y][x] != '#': mat[2*folding_along - y][x] = mat[y][x]
                
                mat = mat[:folding_along][:]    # removing folded rows

                y_max = folding_along

            #return sum([row.count('#') for row in mat]) # --> to solve part1

    return mat # --> to solve part2          

if __name__ == "__main__":
    
    #print(day13())                 # --> to print part1 result
    for row in day13():             # --> to print part2 result
        for c in row:
            print(c, end='')
        print()
