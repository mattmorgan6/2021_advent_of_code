from typing import DefaultDict


def part_2():
    data = []
    mappy = DefaultDict(lambda: [])

    with open('input.txt', 'r') as f:
        lines = list(f.readlines())
        for l in lines:
            line = l.strip().split('-')
            mappy[line[0]].append(line[1])
            mappy[line[1]].append(line[0])

    print(mappy)
    grand_total = 0

    grand_total = 0

    visited = set()

    def dfs(src, path, used):
        """
        dfs through the graph,
        end always adds 1, doesn't go to other neighbors of end
        """

        if src == "start":
            # If it is lowercase and visited
            return 0

        if used:
            if path.count(src) >= 1:
                if ord(src[0]) >= ord('a'):
                    return 0
        else:
            if path.count(src) >= 2:
                if ord(src[0]) >= ord('a'):
                    return 0

        path.append(src)
        if ord(src[0]) >= ord('a') and path.count(src) >= 2:
            # We are allowed to repeat a small cave twice, so I added this boolean to keep track of if we've used our small cave privelidge yet
            used = True

        count = 0
        for neighbor in mappy[src]:
            if neighbor == "end":
                count += 1
            else:
                r = dfs(neighbor, path.copy(), used)
                count += r

        del path[-1]

        return count

    for neighbor in mappy["start"]:
        visited = set()
        visited.add("start")
        res = dfs(neighbor, ["start"], False)
        grand_total += res

    return grand_total


print(part_2())


# def part_1():
#     data = []
#     mappy = DefaultDict(lambda: [])

#     with open('input.txt', 'r') as f:
#         lines = list(f.readlines())
#         for l in lines:
#             line = l.strip().split('-')
#             mappy[line[0]].append(line[1])
#             mappy[line[1]].append(line[0])


#     print(mappy)
#     # print(data)
#     # print()
#     grand_total = 0

#     grand_total = 0

#     visited = set()
#     def dfs(src, path):
#         """
#         dfs through the graph,
#         add 1 if it returns to a big cave, else add 0
#         end always returns, doesn't go to other neighbors

#         visited = start, A, b
#         A: 2
#         b:
#         A:
#         c:


#         """

#         if src in path:
#             if src == "start":
#                 # If it is lowercase and visited
#                 return 0
#             elif ord(src[0]) >= ord('a'):
#                 return 0

#         path.append(src)

#         count = 0
#         for neighbor in mappy[src]:
#             if neighbor == "end":
#                 count += 1
#             else:
#                 path.append(src)
#                 r = dfs(neighbor, path.copy())

#                 count += r

#         del path[-1]

#         return count

#     for neighbor in mappy["start"]:
#         visited = set()
#         visited.add("start")
#         res = dfs(neighbor, ["start"])
#         grand_total += res

#     return grand_total


# print(part_1())
