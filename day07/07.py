import numpy as np

def day07_a():

    with open('in.txt') as f:
        p = np.array([int(el) for el in f.readline().split(',')])

    return int(np.sum(np.abs(np.subtract(p, np.median(p)))))

def day07_b():

    with open('in.txt') as f:
        p = np.array([int(el) for el in f.readline().split(',')])
        mean = int(np.mean(p))

    return int(np.sum(np.apply_along_axis(lambda x : 0.5 * (abs(mean-x) * (abs(mean-x)+1)), 0, p)))

if __name__ == "__main__":
    print(day07_a())
    print(day07_b())
