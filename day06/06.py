def day06():

    # days = 80  to solve part 1
    # days = 256 to solve part 2
    
    days = 80

    with open('in.txt') as f:
        
        t = [int(el) for el in f.readline().split(',')]
        state = [len(list(filter(lambda x: x == i, t))) for i in range(7)]

        count_lanternfish, count7, count8 = len(t), 0, 0
        
        for d in range(days):
            temp = state[0]
            state = state[1:] + state[:1]
            state[6] += count7
            count7, count8 = count8, temp
            count_lanternfish += temp 
        
    return count_lanternfish

if __name__ == "__main__": print(day06())
