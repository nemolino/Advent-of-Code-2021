def day05_b():

    d = {}
    
    with open('in.txt') as f:
        
        for line in f:
            
            x1, y1, x2, y2 = [int(x) for x in line.replace(" -> ", ",").split(',')]
            
            if x1 == x2:    # vertical movement case

                if y2 < y1: y1, y2 = y2, y1                     # I always want to make the movement down
                
                while y1 <= y2:
                    if (x1,y1) in d: d[(x1,y1)] += 1
                    else: d[(x1,y1)] = 1
                    y1 += 1

            elif y1 == y2:  # horizontal movement case

                if x2 < x1: x1, x2 = x2, x1                     # I always want to make the movement to the right

                while x1 <= x2:
                    if (x1,y1) in d: d[(x1,y1)] += 1
                    else: d[(x1,y1)] = 1
                    x1 += 1

            elif x2 - x1 == y2 - y1:    # diagonal movement to the right case

                if x1 > x2: x1, x2, y1, y2 = x2, x1, y2, y1     # I always want to make the movement down

                while x1 <= x2:
                        if (x1,y1) in d: d[(x1,y1)] += 1
                        else: d[(x1,y1)] = 1
                        x1 += 1
                        y1 += 1

            elif x2 - x1 == -y2 + y1:   # diagonal movement to the left case
                
                if x1 < x2: x1, x2, y1, y2 = x2, x1, y2, y1     # I always want to make the movement down

                while x1 >= x2:
                        if (x1,y1) in d: d[(x1,y1)] += 1
                        else: d[(x1,y1)] = 1
                        x1 -= 1
                        y1 += 1

    return len([el for el in d.values() if el > 1])

if __name__ == "__main__": print(day05_b())
