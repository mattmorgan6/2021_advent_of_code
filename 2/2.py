# PART 2:  (don't have part 1 because I overwrote it)
def run():

    # read in from file, each line is an int
    with open('input.txt', 'r') as f:
        data = f.readlines()
        # split each data into dir and distance
        data = [line.split(' ') for line in data]

        total_dist, total_depth, aim = 0, 0, 0

        for d in data:
            direction, distance = d[0].strip(), int(d[1].strip())

            if direction == "forward":
                total_dist += distance
                total_depth += aim * distance

            if direction == "up":
                # total_depth -= distance
                aim -= distance

            if direction == "down":
                # total_depth += distance
                aim += distance

            # print(direction, distance)

        return total_dist * total_depth


print(run())