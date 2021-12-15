# No part 1, but it was similar, see line 10
def part_2():
    """
    1. check for corrupted lines and throw them out (first char != last char)

    """
    data = []

    mappy = {'(': ')', '[': ']', '{': '}', '<': '>'}
    # score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score_map = {')': 1, ']': 2, '}': 3, '>': 4}

    with open('input.txt', 'r') as f:
        lines = list(f.readlines())
        for l in lines:
            line = l.strip()
            data.append(line)

    totals = []

    for line in data:

        stack = []
        broke = False
        for c in line:
            if c in mappy:
                stack.append(mappy[c])
            else:
                if stack[-1] == c:
                    stack.pop()
                else:
                    broke = True
                    # total += score_map[c]
                    # print(stack, c, score_map[c])
                    break

        if not broke and len(stack) > 0:
            total = 0
            stack.reverse()
            for c in stack:
                total *= 5
                total += score_map[c]
            # print(total)
            totals.append(total)

    totals.sort()

    return totals[len(totals) // 2]


print(part_2())
