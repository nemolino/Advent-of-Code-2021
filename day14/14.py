import copy

def day14():

    rules, pol_state = {}, {}
    
    with open('in.txt') as f:

        pol, _ = f.readline().strip(), f.readline()
        
        for line in f:
            start, end = line.strip().split(' -> ')
            rules[start] = (start[0]+end, end+start[1])
            pol_state[start], pol_state[start[0]+end], pol_state[end+start[1]] = 0, 0, 0

    initial_pol_state = copy.deepcopy(pol_state)
        
    for i in range(2, len(pol)+1): pol_state[ pol[i-2:i] ] = 1

    #for step in range(10):  # --> to solve part1
    for step in range(40):  # --> to solve part2
        
        keys_to_add = copy.deepcopy(initial_pol_state)
        
        for k in pol_state.keys():
            keys_to_add[ rules[k][0] ] += pol_state[k]
            keys_to_add[ rules[k][1] ] += pol_state[k]
            pol_state[k] = 0
            
        for k in keys_to_add.keys(): pol_state[k] += keys_to_add[k]

    count = {key[0]:0 for key in pol_state.keys()}
    for (key, value) in pol_state.items(): count[key[0]] += value
    count[pol[-1]] += 1 # adding the last letter to count
    
    return max(count.values()) - min(count.values())        

if __name__ == "__main__": print(day14())
