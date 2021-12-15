from typing import no_type_check_decorator

# PART 2 INCOMPLETE - WRONG ANSWER
def part_2():
    """
    dfs from top left (0,0) to bottom right
    use a scores array to keep track of visited and how much it costs to travel to there
    
    """

    data = []

    with open('input.txt', 'r') as f:
        lines = list(f.readlines())
        for l in lines:
            data.append(list(map(int, list(l.strip()))))

    visited = set()
    n_rows = len(data)
    n_cols = len(data[0])

    # Copy big_data 5 times wide and 5 times height
    big_data = data.copy()
    for r in range(len(big_data)):
        big_data[r] = big_data[r] * 5

    for i in range(4):
        for j in range(n_rows):
            big_data.append([])
            for c in range(len(big_data[0])):
                big_data[-1].append(int(big_data[j][c]))

    # print(big_data[:10])
    # big_data = [[0 for c in range(n_cols * 5)] for r in range(n_rows * 5)]
    
    for i in range(5):
        for j in range(5):
            for r in range(0, len(data)):
                for c in range(0, len(data[0])):
                    if i == 0 and j == 0:
                        break
                    temp_r = r + n_rows * i
                    temp_c = c + n_cols * j
                    big_data[temp_r][temp_c] += i + j
                    if big_data[temp_r][temp_c] >= 10:
                        big_data[temp_r][temp_c] -= 9

                # print(big_data[0])

    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    data = big_data

    scores = [[9 for c in range(len(data[0]))] for r in range(len(data))]
    
    scores[0][0] = data[0][0]
    for c in range(1, len(data[0])):
        scores[0][c] = scores[0][c - 1] + data[0][c]
    for r in range(1, len(data)):
        if r == 10:
            s = ''
        scores[r][0] = scores[r - 1][0] + data[r][0]

    for r in range(1, len(data)):
        if r == 10:
            s = ''
        for c in range(1, len(data[0])):
            scores[r][c] = min(scores[r-1][c], scores[r][c-1]) + data[r][c]

    # for r in scores:
    #     print(r[:20])

    return scores[-1][-1] - scores[0][0]
    

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

