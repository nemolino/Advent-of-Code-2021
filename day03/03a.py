import numpy as np

def day03_a():
    
    n = 12 # number of digits for each row
    line_count_bound, gamma, epsilon = 0, 0, 0
    counter = np.zeros((12,), dtype=int)
    
    with open('in.txt') as f:
        
        for line in f:
            line_count_bound += 1
            counter += np.array(list(line.strip()), dtype=int)
            
        line_count_bound /= 2
        
        for i in range(n-1, -1, -1):
            if counter[i] > line_count_bound: gamma += 2**(n-1-i)
            else: epsilon += 2**(n-1-i)
            
    return gamma * epsilon

if __name__ == "__main__": print(day03_a())
