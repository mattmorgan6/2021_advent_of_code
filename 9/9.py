def part_2():
    """
    dfs from each low point
    
    """
    data = []

    with open('input.txt', 'r') as f:
        lines = list(f.readlines())
        for l in lines:
            data.append(list(map(int, list(l.strip()))))

    total = 0
    low_points = []
    
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for r in range(len(data)):
        for c in range(len(data[0])):
            correct = True
            for dx, dy in dirs:
                n_x = c + dx
                n_y = r + dy
                if 0 <= n_x < len(data[0]) and 0 <= n_y < len(data):
                    if data[r][c] >= data[n_y][n_x]:
                        correct = False
                        break

            if correct:
                total += data[r][c] + 1
                low_points.append((r,c))

 
    visited = set()

    def dfs(r, c):
        if (r, c) in visited:
            return 0

        if data[r][c] == 9:
            return 0

        # print(f'{r},{c} = {data[r][c]}')

        visited.add((r, c))
        temp = 0
        for dx, dy in dirs:
            n_x = c + dx
            n_y = r + dy
            if 0 <= n_x < len(data[0]) and 0 <= n_y < len(data):
                if data[r][c] < data[n_y][n_x]:
                    temp += dfs(n_y, n_x)

        return temp + 1


    results = []
    for y, x in low_points:
        r = dfs(y,x)
        results.append(r)

    results.sort()
    print(results)
    print(results[-1] * results[-2] * results[-3])

    return total

print(part_2())




# def part_1():
#     """
#     Find all the low points,
#     add one to each and return sum
    
#     """
#     data = []

#     with open('input.txt', 'r') as f:
#         lines = list(f.readlines())
#         for l in lines:
#             data.append(list(map(int, list(l.strip()))))

#     total = 0
#     print(data)
    
#     dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
#     for r in range(len(data)):
#         for c in range(len(data[0])):
#             correct = True
#             for dx, dy in dirs:
#                 n_x = c + dx
#                 n_y = r + dy
#                 if 0 <= n_x < len(data[0]) and 0 <= n_y < len(data):
#                     if data[r][c] >= data[n_y][n_x]:
#                         correct = False
#                         break

#             if correct:
#                 total += data[r][c] + 1




#     return total

# print(part_1())

