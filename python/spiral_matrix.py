def spiral_print(matrix):
    cols = len(matrix)
    rows = len(matrix[0])

    start_x = 0
    start_y = 0
    end_x = rows - 1
    end_y = cols - 1

    for layer in xrange(min(rows, cols)/2+1):

        for top_row in xrange(start_x, end_x):
            print matrix[start_y][top_row]

        for right_col in xrange(start_y, end_y):
            print matrix[right_col][end_x]

        if start_x == end_x:
            # Matrix is a col vector
            print matrix[end_y][end_x]
            break

        if start_y == end_y:
            # Matrix is a row vector
            print matrix[start_y][end_x]
            break

        for bottom_row in xrange(end_x, start_x, -1):
            print matrix[end_y][bottom_row]

        for left_col in xrange(end_y, start_y, -1):
            print matrix[left_col][start_x]

        start_x += 1
        start_y += 1
        end_x -= 1
        end_y -= 1



print spiral_print([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print spiral_print([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14 ,15],
              [16, 17, 18, 19, 20]])

print spiral_print([[1, 2, 3, 4, 5]])

print spiral_print([[1],
              [6],
              [11],
              [16]])