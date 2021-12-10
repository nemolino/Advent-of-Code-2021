from collections import deque

delimiters = {')' : ('(', 3, 1), ']' : ('[', 57, 2), '}' : ('{', 1197, 3), '>' : ('<', 25137, 4)}

def line_check(line):
    
    stack = deque([])
    
    for c in line:
        if c in [d[0] for d in delimiters.values()]:
            stack.append(c)
        elif stack.pop() != delimiters[c][0]:
            return delimiters[c][1]
    return 0

def day10_a():

    with open('inprova.txt') as f:
        return sum([line_check(line.strip()) for line in f])

def line_score(line):
    
    stack = deque([])
    
    for c in line:
        if c in [d[0] for d in delimiters.values()]:
            stack.append(c)
        elif stack.pop() != delimiters[c][0]:
            return False
        
    score = 0
    while len(stack) > 0:
        popped = stack.pop()
        score = score * 5 + [d[2] for d in delimiters.values() if d[0] == popped][0]  
    return score
    
def day10_b():
    
    with open('in.txt') as f:
        scores = []
        for line in f:
            s = line_score(line.strip())
            if s: scores.append(s)

        return sorted(scores)[len(scores) // 2]

if __name__ == "__main__":
    print(day10_a())
    print(day10_b())







