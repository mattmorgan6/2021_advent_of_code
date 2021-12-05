def part_1_and_2():

    # read in from file, each line is an int
    with open('sample.txt', 'r') as f:

        lines = []
        minX, minY, maxX, maxY = 0, 0, 0, 0
        while True:
            data = f.readline()
            if not data:
                break

            coords = data.strip().split('->')
            x1, y1 = coords[0].strip().split(',')
            x2, y2 = coords[1].strip().split(',')
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            if x1 == x2 or y1 == y2:
                if x1 == x2:
                    if y2 < y1:
                        y1, y2 = y2, y1
                else:
                    if x2 < x1:
                        x1, x2 = x2, x1

            lines.append([x1, y1, x2, y2])
            minX = min(minX, x1, x2)
            maxX = max(maxX, x1, x2)
            minY = min(minY, y1, y2)
            maxY = max(maxY, y1, y2)


        grid = [[0 for i in range(maxX - minX + 1)] for j in range(maxY - minY + 1)]
        

        for x1, y1, x2, y2 in lines:
            if x1 == x2:
                # vertical line
                for r in range(y1, y2 + 1):
                    grid[r - minY][x1 - minX] += 1

            elif y1 == y2:
                # horizontal line
                for c in range(x1, x2 + 1):
                    grid[y1 - minY][c - minX] += 1

            else:
                if x2 > x1:
                    if y2 > y1:
                        # goes from left to right and down
                        for i in range(y2 - y1 + 1):
                            grid[y1 - minY + i][x1 - minX + i] += 1

                    else:
                        # goes from left to right and up
                        for i in range(y1 - y2 + 1):
                            grid[y1 - minY - i][x1 - minX + i] += 1
                else:
                    if y2 > y1:
                        # goes right to left and up
                        for i in range(y2 - y1 + 1):
                            grid[y1 - minY + i][x1 - minX - i] += 1
                        pass
                    else:
                        # goes from right to left and up
                        for i in range(y1 - y2 + 1):
                            grid[y2 - minY + i][x2 - minX + i] += 1
                        pass
        
        # print(grid)
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] >= 2:
                    count += 1

        return count

print(part_1_and_2())