def day03_b():

    n = 12 # number of digits for each row
    f = open('in.txt')
    oxygen = list(f)
    co2 = oxygen
    
    for i in range(n):

        if len(oxygen) > 1:
            oxygen_0 = list(filter(lambda x: x[i] == '0', oxygen))
            oxygen_1 = list(filter(lambda x: x[i] == '1', oxygen))
            oxygen = oxygen_1 if len(oxygen_1) >= len(oxygen_0) else oxygen_0
                
        if len(co2) > 1:
            co2_0 = list(filter(lambda x: x[i] == '0', co2))
            co2_1 = list(filter(lambda x: x[i] == '1', co2))
            co2 = co2_1 if len(co2_1) < len(co2_0) else co2_0
            
    f.close() 
    return int(oxygen[0].strip(), 2) * int(co2[0].strip(), 2)

if __name__ == "__main__": print(day03_b())
