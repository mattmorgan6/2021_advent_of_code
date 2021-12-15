import collections
from typing import DefaultDict

# PART 2 INCOMPLETE - WRONG ANSWER
def part_2():
    """
    Template:     NNCB
    After step 1: NCNBCHB
    After step 2: NBCCNBBBCBHCB
    After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
    After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB


    NN + CN

    ...
    2 becomes 3 becomes 5 becomes 9 becomes 17
    The formula is new_x = (2*x) - 1

    Once we reach a cycle, can we break?
    How do we memoize this? Can we memoize every block of 6 characters?
    """

    d_map = {}
    start_str = ""

    with open('sample.txt', 'r') as f:
        start_str = f.readline().strip()
        skip = f.readline()
        line = f.readline().strip().split('->')
        while len(line) > 1:
            src, dst = line[0].strip(), line[1].strip()
            d_map[src] = dst
            line = f.readline().strip().split('->')

    total = 2
    
    memo = {}

    old_s = list(start_str)

    def recurse(i, j, k, count):
        """
        given three characters, call recurse(0,1) + recurse(1,2)
        """
        count += 1
        if count > total:
            return i+j

        t1 = d_map[i+j]
        t2 = d_map[j+k]
        
        r1 = ''
        if (i+t1) in memo:
            r1 = memo[i+t1]
            print("here1", r1)
            r1 = recurse(i, t1, j, count)
            print("here2", r1)
        else:
            r1 = recurse(i, t1, j, count)

        r2 = recurse(j, t2, k, count)
        
        memo[i+j] = r1
        memo[j+k] = r2
        
        return r1 + r2

    result1 = recurse('N', 'N', 'C', 0)
    # print(result1)
    result2 = recurse('N', 'C', 'B', 0)[2**total:] + start_str[-1]
    # print(result2)
    print(result1 + result2)
    print()
    print(memo)


    old_s = list(result1 + result2)

    freq = DefaultDict(lambda: 0)
    max_f = min_f = 0
    max_c = min_c = 0
    for c in old_s:
        freq[c] += 1

    for k, v in freq.items():
        if max_f == 0:
            max_f = v
            max_c = k
            min_f = v
            min_c = k

        if freq[k] > max_f:
            max_f = freq[k]
            max_c = v
        if freq[k] < min_f:
            min_f = freq[k]
            min_c = v

    print()
    print(max_f, min_f)
    return max_f - min_f



print(part_2())




# def part_1():
#     """
#     Template:     NNCB
#     After step 1: NCNBCHB
#     After step 2: NBCCNBBBCBHCB
#     After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
#     After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
#     ...
#     2 becomes 3 becomes 5 becomes 9 becomes 17
#     The formula is new_x = (2*x) - 1

#     Once we reach a cycle, can we break?
#     How do we memoize this? Can we memoize every block of 6 characters?
#     """

#     d_map = {}
#     start_str = ""

#     with open('sample.txt', 'r') as f:
#         start_str = f.readline().strip()
#         skip = f.readline()
#         line = f.readline().strip().split('->')
#         while len(line) > 1:
#             src, dst = line[0].strip(), line[1].strip()
#             d_map[src] = dst
#             line = f.readline().strip().split('->')

    
#     memo = {}

#     old_s = list(start_str)
#     for j in range(3):
#         if j % 2 == 0:
#             print(''.join(old_s), len(old_s))
#             x = 1
#             i = 0
#             while x < len(old_s):
#                 x -= 1
#                 # print(start_str[i:i+2], old_s[x:x+5])
#                 memo[start_str[i:i+2]] = old_s[x:x+5]
#                 x += 5
#                 i += 1

#             print(memo)


#         new_s = []
#         for i in range(len(old_s) - 1):
#             t = old_s[i] + old_s[i+1]
#             if t in memo:
#                 print("here")

#             new_s.append(old_s[i])
#             new_s.append(d_map[t])
#         new_s.append(old_s[-1])
#         old_s = new_s
#         # print(''.join(old_s))

#     freq = DefaultDict(lambda: 0)
#     max_f = min_f = 0
#     max_c = min_c = 0
#     for c in old_s:
#         freq[c] += 1

#     for k, v in freq.items():
#         if max_f == 0:
#             max_f = v
#             max_c = k
#             min_f = v
#             min_c = k

#         if freq[k] > max_f:
#             max_f = freq[k]
#             max_c = v
#         if freq[k] < min_f:
#             min_f = freq[k]
#             min_c = v
    
#     print(max_f, min_f)
#     return max_f - min_f



# print(part_1())
