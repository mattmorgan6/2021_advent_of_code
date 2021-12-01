# PART 2:
def run():
    """
    three-measurement sliding window, compare sums
    """

    # read in from file, each line is an int
    with open('input.txt', 'r') as f:
        data = f.readlines()
        # strip each string in data and convert to int
        data = [int(x.strip()) for x in data]

        count = 0
        prev = float('inf')
        for i in range(1, len(data) - 1):
            # get sum of three elements
            sum_three = data[i-1] + data[i] + data[i+1]
            if sum_three > prev:
                count += 1
            prev = sum_three

        return count



print(run())




# # PART 1:
# def run():
#     """
#     returns the # of times a measurement increases (int)
#     """

#     # read in from file, each line is an int
#     with open('input.txt', 'r') as f:
#         data = f.readlines()
#         # strip each string in data and convert to int
#         data = [int(x.strip()) for x in data]
#
#         count = 0
#         for i in range(len(data) - 1):
#             if data[i] < data[i + 1]:
#                 count += 1
#         return count

# print(run())

