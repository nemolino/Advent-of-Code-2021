import numpy as np

def day11():

    with open('in.txt') as f:

        m = [[0]*12]
        for el in [[0] + [int(el) for el in line.strip()] + [0] for line in f]: m.append(el)
        m.append([0]*12)

        m = np.array( m, dtype = np.uint16)
        
        step, flashes_count = 0, 0
        
        while True:
            
            m = m+1
            t = []
            
            while True:

                flag = True
                
                for i in range(1,11):
                    for j in range(1,11):
                        if m[i][j] > 9 and (i,j) not in t:
                            
                            flag = False
                            t.append((i,j))
        
                            if (i-1,j-1) not in t:  m[i-1][j-1] += 1
                            if (i-1,j) not in t:    m[i-1][j]   += 1
                            if (i-1,j+1) not in t:  m[i-1][j+1] += 1
                            if (i,j-1) not in t:    m[i][j-1]   += 1
                            if (i,j+1) not in t:    m[i][j+1]   += 1
                            if (i+1,j-1) not in t:  m[i+1][j-1] += 1
                            if (i+1,j) not in t:    m[i+1][j]   += 1
                            if (i+1,j+1) not in t:  m[i+1][j+1] += 1
                            
                if flag == True: break
                
            for el in t: m[el[0]][el[1]] = 0

            # to solve part1
            #if step < 100: flashes_count += len([1 for i in range(1,11) for j in range(1,11) if m[i][j] == 0])
            #else: return flashes_count

            # to solve part2
            flag = 1
            for i in range(1,11):
                for j in range(1,11):
                    if m[i][j] != 0:
                        flag = 0
                        break
            if flag: return step+1
            
            step += 1

if __name__ == "__main__": print(day11())
