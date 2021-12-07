def day07_a():

    with open('in.txt') as f:
        
        p = sorted([int(el) for el in f.readline().split(',')])
        len_p = len(p)
        center = int( 0.5 * ( p[int(len_p/2-1)] + p[int(len_p/2)] ) )

    return sum([ abs(center-el) for el in p])

def day07_b():

    with open('in.txt') as f:
        
        p = [int(el) for el in f.readline().split(',')]
        mean = int(sum(p)/len(p))

    return int( sum([0.5 * (abs(mean-el) * (abs(mean-el)+1)) for el in p]) )

if __name__ == "__main__":
    print(day07_a())
    print(day07_b())
