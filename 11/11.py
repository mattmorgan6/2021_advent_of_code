def part_2():
    data = []

    with open('input.txt', 'r') as f:
        lines = list(f.readlines())
        for l in lines:
            line = l.strip()
            data.append(list(map(int, line)))

    dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
    # print(data)
    # print()
    grand_total = 0

    def dfs(r, c, visited):
        visited.add((r,c))
        count = 0
        for dy, dx in dirs:
            n_x, n_y = c + dx, r + dy
            if 0 <= n_x < n_cols and 0 <= n_y < n_rows:
                if data[n_y][n_x] == 9:
                    data[n_y][n_x] = 0
                    count += 1
                    count += dfs(n_y, n_x, visited)
                elif data[n_y][n_x] == 0:
                    pass
                else:
                    data[n_y][n_x] += 1

        return count

    n_rows = len(data)
    n_cols = len(data[0])

    total = 0
    for steps in range(1000):
        for r in range(n_rows):
            for c in range(n_cols):
                if data[r][c] == 9:
                    data[r][c] = 0
                else:
                    data[r][c] += 1

        visited = set()
        for r in range(n_rows):
            for c in range(n_cols):
                if data[r][c] == 0 and (r,c) not in visited:
                    total += dfs(r,c,visited)

        x = sum([sum(r) for r in data])
        if x == 0:
            return steps + 1

    return "no dice"


print(part_2())


# def part_1():
#     """
#     1. check for corrupted lines and throw them out (first char != last char)

#     """
#     data = []

#     with open('input.txt', 'r') as f:
#         lines = list(f.readlines())
#         for l in lines:
#             line = l.strip()
#             data.append(list(map(int, line)))

#     dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
#     # print(data)
#     # print()
#     grand_total = 0

#     def dfs(r, c, visited):
#         visited.add((r,c))
#         count = 0
#         for dy, dx in dirs:
#             n_x, n_y = c + dx, r + dy
#             if 0 <= n_x < n_cols and 0 <= n_y < n_rows:
#                 if data[n_y][n_x] == 9:
#                     data[n_y][n_x] = 0
#                     count += 1
#                     count += dfs(n_y, n_x, visited)
#                 elif data[n_y][n_x] == 0:
#                     pass
#                 else:
#                     data[n_y][n_x] += 1

#         return count

#     n_rows = len(data)
#     n_cols = len(data[0])

#     total = 0
#     for steps in range(100):
#         for r in range(n_rows):
#             for c in range(n_cols):
#                 if data[r][c] == 9:
#                     data[r][c] = 0
#                 else:
#                     data[r][c] += 1

#         visited = set()
#         for r in range(n_rows):
#             for c in range(n_cols):
#                 if data[r][c] == 0 and (r,c) not in visited:
#                     total += dfs(r,c,visited)

#         # print(data)
#         # print()
#         for r in data:
#             for c in r:
#                 if c == 0:
#                     grand_total += 1
#         # print(f'{i}: {grand_total}')
#         # print()

#     return grand_total


# print(part_1())
