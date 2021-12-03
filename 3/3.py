# PART 2:
def part_2():
    """
    Story:
        Find oxygen and CO2 ratings multipied.

    Algo:
        loop col data is of len(1):
            for oxygen:
                get the most common bit
                add it to c_gamma
                remove all the nums in data where d[col] != most common bit
            for co2:
                opposite

        add the rest of d[0] to c_gamma

        return gamma * epsilon
    """

    # read in from file, each line is an int
    with open('input.txt', 'r') as f:
        data = f.readlines()
        # strip each line of data
        data = [x.strip() for x in data]

        # stores current/best
        c_gamma = []
        c_epsilon = []

        d_gamma = data.copy()
        d_epsilon = data.copy()

        l = len(data[0])
        for col in range(l):
            if len(d_gamma) == 1:
                c_gamma += list(map(int, d_gamma[0][col:]))
                break

            ones = 0
            zeros = 0
            for d in d_gamma:
                if d[col] == '1':
                    ones += 1
                else:
                    zeros += 1

            if ones >= zeros:
                c_gamma.append(1)
            else:
                c_gamma.append(0)

            # remove all the nums in data where d[col] != most common bit
            i = 0
            while i < len(d_gamma):
                if int(d_gamma[i][col]) != c_gamma[col]:
                    d_gamma.pop(i)
                else:
                    i += 1

        for col in range(l):
            if len(d_epsilon) == 1:
                c_epsilon += list(map(int, d_epsilon[0][col:]))
                break

            ones = 0
            zeros = 0
            for d in d_epsilon:
                if d[col] == '1':
                    ones += 1
                else:
                    zeros += 1

            if ones < zeros:
                c_epsilon.append(1)
            else:
                c_epsilon.append(0)

            # remove all the nums in data where d[col] != most common bit
            i = 0
            while i < len(d_epsilon):
                if int(d_epsilon[i][col]) != c_epsilon[col]:
                    d_epsilon.pop(i)
                else:
                    i += 1

        s = ''.join(map(str, d_gamma))
        gamma = int(s, 2)

        s = ''.join(map(str, c_epsilon))
        epsilon = int(s, 2)

        return gamma * epsilon


print(part_2())


# PART 1:
def part_1():

    # read in from file, each line is an int
    with open('input.txt', 'r') as f:
        data = f.readlines()
        # strip each line of data
        data = [x.strip() for x in data]

        # binary and each d in data
        gamma = 11111
        # epsilon = 0

        c_gamma = []

        l = len(data[0])
        for col in range(l):
            ones = 0
            zeros = 0
            for d in data:
                if d[col] == '1':
                    ones += 1
                else:
                    zeros += 1
            if ones > zeros:
                c_gamma.append(1)
            else:
                c_gamma.append(0)

        s = ''.join(map(str, c_gamma))
        gamma = int(s, 2)

        str_epsilon = ''
        for c in s:
            if c == '1':
                str_epsilon += '0'
            else:
                str_epsilon += '1'

        epsilon = int(str_epsilon, 2)

        return gamma * epsilon

# print(part_1())
