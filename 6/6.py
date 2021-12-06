def part_2():

    # O(# total_days * 9) time complexity -> O(n)
    # O(9) space complexity -> constant

    with open('input.txt', 'r') as f:

        data = f.readline().strip().split(',')
        data = list(map(int, data))

        # keeps track of how many fish are in each stage of life
        buckets = [0 for _ in range(10)]

        for fish_life in data:
            buckets[fish_life] += 1

        total_days = 256
        for day in range(total_days):
            for idx, count in enumerate(buckets):
                if idx == 0:
                    # we use 7 because the enumerate will decrease it to 6 in the current iter.
                    buckets[7] += count
                    buckets[9] += count
                    buckets[idx] = 0
                else:
                    buckets[idx - 1] += count
                    buckets[idx] = 0

        return sum(buckets)

print(part_2())


def part_1():

    # O(# total_days * # of fish) time complexity -> O(n*m)
    # O(# of fish) space complexity -> O(m)

    with open('sample.txt', 'r') as f:

        data = f.readline().strip().split(',')
        data = list(map(int, data))

        total_days = 18
        for day in range(total_days):
            for idx, life in enumerate(data):
                if life == 0:
                    data[idx] = 6
                    # we use 9 because the enumerate will pick it up then decrease it to 8.
                    data.append(9)
                else:
                    data[idx] -= 1

        return len(data)


# print(part_1())
