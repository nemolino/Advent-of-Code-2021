from updateable_queue import UpdateableQueue
import math

def dijkstra_algorithm(m):

    nrows, ncols = len(m), len(m[0])
    
    # vertices
    V = [(i,j) for i in range(nrows) for j in range(ncols)]

    # adjacency list
    E = {}
    for v in V:
        i, j = v
        E[v] = []
        if i > 0: E[v].append( ((i-1,j), m[i-1][j]) )
        if i < nrows-1: E[v].append( ((i+1,j), m[i+1][j]) )
        if j > 0: E[v].append( ((i,j-1), m[i][j-1]) )
        if j < ncols-1: E[v].append( ((i,j+1), m[i][j+1]) )

    d = {v : math.inf for v in V}   # vector of distances
    d[(0,0)] = 0

    C = UpdateableQueue()           # set of candidates vertices implemented with priority queue
    for v in V: C.push(v, d[v])

    while len(C) > 0:
        
        u_vertex, u_priority = C.pop()
        
        for edge in E[u_vertex]:
            if d[u_vertex] + edge[1] < d[edge[0]]:
                d[edge[0]] = d[u_vertex] + edge[1]
                C.push(edge[0], d[edge[0]])
                
    return d[(nrows-1, ncols-1)]
    
def day15_a():
    
    with open('in.txt') as f:
        m = [[int(el) for el in line.strip()] for line in f]
        
    return dijkstra_algorithm(m)
    

def day15_b():

    with open('in.txt') as f:
        m = [[int(el) for el in line.strip()] for line in f]
        
    nrows = len(m)
    for step in range(4):
        for i in range(nrows):
            m.append([ el+1 if el+1 != 10 else 1 for el in m[step*nrows+i] ])

    ncols = len(m[0])
    for i in range(len(m)):
        for step in range(4):
            m[i].extend([ el+1 if el+1 != 10 else 1 for el in m[i][step*ncols:] ])

    return dijkstra_algorithm(m)   

if __name__ == "__main__":
    print(day15_a())
    print(day15_b())
