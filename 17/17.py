

# Part 2 only, part 1 is very similar though
def part_2():
    """
    Formula: 

    x_vel = 1
    y_vel = 1

    result_x = x_vel - step, assuming x_vel is positive
    result_y = y_vel - step

    we want to maximze the y_vel to get the most distance.

    we want x_vel to equal 0 when it is above the x_end_num.
    the x_pos is a decreasing series function that we want to end at 0 in the target.
    So consider it an increasing series function that ends at 0.

    For each x_val in the target, see if we can get an increasing series function that ends at 0.

    Start with brute force <-- brute force works

    """
    
    def get_input():
        with open('input.txt', 'r') as f:
            line = f.readline().strip().split(' ')
            x_str = line[-2]
            y_str = line[-1]

            x_toks = x_str.split('..')
            x_start_num = int(x_toks[0][2:])
            x_end_num = int(x_toks[1][:-1])

            y_toks = y_str.split('..')
            y_start_num = int(y_toks[0][2:])
            y_end_num = int(y_toks[1])

            return x_start_num, x_end_num, y_start_num, y_end_num

    # Target values
    x_start_num, x_end_num, y_start_num, y_end_num = get_input()

    x_pos = y_pos = 0

    start_x_vel = 6
    start_y_vel = 3
    
    best_x_vel = 0
    best_y_vel = 0
    i = 0

    highest = 0
    setty = set()

    for a in range(-300,400):
        for b in range(-300,400):
            i += 1
            x_pos = 0
            y_pos = 0
            start_x_vel = a
            start_y_vel = b
            x_vel = a
            y_vel = b

            temp_highest = 0

            while True:
                x_pos += x_vel
                y_pos += y_vel
                
                
                temp_highest = max(temp_highest, y_pos)
                if x_start_num <= x_pos <= x_end_num and y_start_num <= y_pos <= y_end_num:
                    found = True
                    # print("Best_x_vel: ", start_x_vel)
                    # print("Best_y_vel: ", start_y_vel)
                    setty.add((start_x_vel, start_y_vel))
                    if start_y_vel > best_y_vel:
                        best_y_vel = start_y_vel
                        best_x_vel = start_x_vel
                        highest = max(temp_highest, highest)

                    break

                if x_pos > x_end_num:
                    # print("x too far")
                    break
                if y_pos < y_start_num:
                    # print("x too far")
                    break

            
                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1
        
                y_vel -= 1


    return best_x_vel, best_y_vel, highest, setty


a, b, c, d = part_2()
print(len(d))
