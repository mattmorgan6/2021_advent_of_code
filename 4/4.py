# PART 2:
def part_1_and_2():
    """
    Story:
        Design bingo
    """

    # read in from file, each line is an int
    with open('input.txt', 'r') as f:
        data = f.readlines()
        # strip each line of data
        data = [x.strip() for x in data]

        nums = data[0].split(',')
        nums = list(map(int, nums))
        
        all_boards = []
        all_marks = []

        i = 1
        while i < len(data) - 1:
            i += 1
            board = []
            for j in range(5):
                line = data[i+j].split()
                line = [x.strip() for x in line]

                # map line to ints
                line = list(map(int, line))
                board.append(line)
                
            i += 5
            all_boards.append(board)
            marks = [[False for x in range(5)] for y in range(5)]
            all_marks.append(marks)


        unmarked_sum = 0
        curr_num = 0
        n = 0
        # keeps track of the boards that win so we don't update those anymore
        winning_boards = set()
        # game_over = False

        # draw each num from nums
        for l, num in enumerate(nums):

            # update marks for each board
            for i, board in enumerate(all_boards):
                for j, row in enumerate(board):
                    for k, col in enumerate(row):
                        if col == num:
                            # if j == 0 and k == 1:
                                # print("HERRE", i, num)

                            all_marks[i][j][k] = True

            # check for winners in all_marks
            # check rows, columns, diagonals
            for i, board in enumerate(all_marks):
                done = False
                # check rows
                for j, row in enumerate(board):
                    if all(row):
                        # print('winner in row', i, j)
                        done = True
                        break
                # check columns
                for j, col in enumerate(zip(*board)):
                    if all(col):
                        # print('winner in column', i, j)
                        done = True
                        break

                if done:
                    winning_boards.add(i)
                    if len(winning_boards) == len(all_boards):
                        n = i
                        break
                    

            # end game condition
            if len(winning_boards) == len(all_boards):
                win_board = all_marks[n]
                curr_num = nums[l]
                                
                # sum all the unmarked numbers in board
                for j, row in enumerate(win_board):
                    for k, col in enumerate(row):
                        if not win_board[j][k]:
                            unmarked_sum += all_boards[n][j][k]
  
                return unmarked_sum * curr_num


        
        return unmarked_sum * curr_num

print(part_1_and_2())