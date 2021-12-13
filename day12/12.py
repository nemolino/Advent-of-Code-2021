def day12():

    adj, nodes, count = [], [], 0
    
    with open('in.txt') as f:
        for line in f:
            a, b = line.strip().split('-')
            nodes.append(a)
            nodes.append(b)
            if a != 'end' and b != 'start': adj.append((a,b))
            if a != 'start' and b != 'end': adj.append((b,a))
    nodes = sorted(list(set(nodes)))


    def calc_rec(current_edge, visited_nodes, double_visited = False):
        
        nonlocal count
        visited_nodes.append(current_edge[1])
        
        if current_edge[1] == 'end':
            #print(visited_nodes)
            count += 1
            return

        for edge in adj:
            if edge[0] == current_edge[1]:
                c1, c2 = any(c for c in edge[1] if c.islower()), edge[1] in visited_nodes
                if not (c1 and c2): calc_rec(edge, visited_nodes[:], double_visited)
                elif (c1 and c2 and double_visited == False): calc_rec(edge, visited_nodes[:], True) # --> comment this line to solve part1
        return 
        
        
    for edge in adj:
        if edge[0] == 'start': calc_rec(edge, [edge[0]])

    return count
            

if __name__ == "__main__": print(day12())
