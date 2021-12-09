def day08_a():

    with open('in.txt') as f:
        return sum( [sum([1 for el in line.split('|')[1].split() if len(el) in [2,3,4,7]]) for line in f] )
    
def decode(line):

    # ordino in una lista i pattern per lunghezza e ordino le lettere al loro interno alfabeticamente
    patterns = sorted([''.join(sorted(pattern)) for pattern in line.split('|')[0].split()], key = len)

    mappings = [None]*10

    # i pattern di lunghezza 2, 3, 4, 7 sono mappati rispettivamente alle cifre 1, 7, 4, 8
    mappings[1], mappings[7], mappings[4], mappings[8] = patterns.pop(0), patterns.pop(0), patterns.pop(0), patterns.pop(6)

    # 3 è il pattern di lunghezza 5 che come insieme intersecato con il mapping di 1 ha cardinalità 2
    mappings[3] = patterns.pop( patterns.index( list(filter(lambda x: len( set(x).intersection( set(mappings[1]) ) ) == 2, patterns[0:3]))[0] ) )
    
    # 2 è il pattern di lunghezza 5 che come insieme intersecato con il mapping di 4 ha cardinalità 2
    mappings[2] = patterns.pop( patterns.index( list(filter(lambda x: len( set(x).intersection( set(mappings[4]) ) ) == 2, patterns[0:2]))[0] ) )
    
    # 5 è il pattern di lunghezza 5 rimanente
    mappings[5] = patterns.pop(0)

    # 6 è il pattern di lunghezza 6 che come insieme intersecato con il mapping di 1 ha cardinalità 1
    mappings[6] = patterns.pop( patterns.index( list(filter(lambda x: len( set(x).intersection( set(mappings[1]) ) ) == 1, patterns))[0] ) )
    
    # 0 è il pattern di lunghezza 6 che come insieme intersecato con il mapping di 5 ha cardinalità 4
    mappings[0] = patterns.pop( patterns.index( list(filter(lambda x: len( set(x).intersection( set(mappings[5]) ) ) == 4, patterns))[0] ) )
    
    # 9 è il pattern di lunghezza 6 rimanente
    mappings[9] = patterns.pop(0)

    # metto in una lista i pattern delle cifre con le lettere al loro interno ordinate alfabeticamente
    digits = [''.join(sorted(pattern)) for pattern in line.split('|')[1].split()]
    
    return int(''.join([str(mappings.index(d)) for d in digits]))

def day08_b():

    with open('in.txt') as f:
        return sum([decode(line) for line in f])

if __name__ == "__main__":
    print(day08_a())
    print(day08_b())
