def get_structures():
    
    """ returns the structures used to solve the puzzles """
    
    with open('in.txt') as f:

        # building drawings
        drawings = [int(d) for d in f.readline().split(",")]
        
        # building boards 
        boards = []
        i = -1
        for line in f:
            if len(line.strip()) == 0:
                i += 1
                boards.append([])
            else:
                boards[i].append([int(x) for x in line.split()])
                
        return (drawings, boards)

def is_winning(board):
    
    """ returns True if the board is a winning one, False otherwise """
    
    for row in board:
        if row.count(None) == 5: return True

    for j in range(5):
        for i in range(5):
            if board[i][j] != None: break
        else: return True
        
    return False

def day04_a():
    
    drawings, boards = get_structures()

    # simulating drawings
    for d in drawings:
        for b in boards:
            for row in b:
                if d in row:
                    row[row.index(d)] = None
                    # finding the first winning board
                    if is_winning(b):
                        return d * sum([sum( list(filter(lambda x: x != None, r)) ) for r in b])
                    
    return False

def day04_b():
    
    drawings, boards = get_structures()
        
    # simulating drawings
    for d in drawings:
        for b in boards:
            for row in b:
                if d in row:
                    row[row.index(d)] = None

        # deleting winning boards until we find the last winning one
        for b in boards:             
            if is_winning(b):
                if len(boards) == 1:
                    return d * sum([sum( list(filter(lambda x: x != None, r)) ) for r in b])
                boards.remove(b)
                                     
    return False

if __name__ == "__main__":
    print(day04_a())
    print(day04_b())
