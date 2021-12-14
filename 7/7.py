def part_2():
    """
    Input:
    16,1,2,0,4,2,7,1,2,14

    x is the number we choose to align to
    abs(x - 16) + abs(x-1) + abs(x-2) + abs(x-0)
    if x is less than the number, then take number - x
    else, take x - number

    so total = 
    x - 1 + x - 2 + x - 0 + x - 2 + x - 1 + x - 2
+   16 - x + 4 - x + 7 - x + 14 - x
    =
    
    """

    with open('input.txt', 'r') as f:
        data = f.readline().strip().split(',')
        data = list(map(int, data))

    cost = [0]
    for i in range(1, max(data) - min(data) + 1):
        cost.append(cost[i-1] + i)

    min_total = float('inf')
    for num in range(min(data), max(data)):
        total = 0
        for n in data:
            total += cost[abs(n - num)]
        # print(f'{num} : {total}')
        min_total = min(total, min_total)


    return min_total

print(part_2())



# def part_1():
#     """
#     Optimization problem:
#     16,1,2,0,4,2,7,1,2,14

#     x is the number we choose to align to
#     abs(x - 16) + abs(x-1) + abs(x-2) + abs(x-0)
#     if x is less than the number, then take number - x
#     else, take x - number

#     so total = 
#     x - 1 + x - 2 + x - 0 + x - 2 + x - 1 + x - 2
# +   16 - x + 4 - x + 7 - x + 14 - x
#     =
    
#     """


#     with open('input.txt', 'r') as f:

#         data = f.readline().strip().split(',')
#         data = list(map(int, data))

#         min_total = float('inf')
#         for num in data:
#             total = 0
#             for n in data:
#                 total += abs(n - num)
#             # print(f'{num} : {total}')
#             min_total = min(total, min_total)


#         return min_total

# print(part_1())
