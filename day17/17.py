# puzzle_input --> target area: x=257..286, y=-101..-57
xt1, xt2, yt1, yt2 = 257, 286, -101, -57

def check_target_area(x, y):

    if x > xt2 or y < yt1: return 0     # --> the probe is not within the target area and will never be
    if x < xt1 or y > yt2: return -1    # --> the probe is not within the target area
    return 1                            # --> the probe is within the target area

def day_17():
    
    count, max_y = 0, 0

    # this bounds for x and y velocity seems to work well
    for x_vel_loop in range(0, xt2+1):
        for y_vel_loop in range(yt1, -yt1): 

            x, y, max_y_step, check, x_vel, y_vel = 0, 0, 0, -1, x_vel_loop, y_vel_loop

            while check == -1:

                #### doing the step
                
                x += x_vel
                y += y_vel
                if x_vel > 0: x_vel -= 1
                elif x_vel < 0: x_vel += 1
                y_vel -= 1
                
                ####

                check = check_target_area(x, y)
                
                if check != 0 and y > max_y_step:
                    max_y_step = y

                if check == 1:
                    count +=1 
                    if max_y_step > max_y:
                        max_y = max_y_step
    
    return (max_y, count)

if __name__ == "__main__":
    part1, part2 = day_17()
    print(part1, part2)
