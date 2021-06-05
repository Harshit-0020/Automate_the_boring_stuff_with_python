def print_table(tabledata):
    col_width = [0] * len(tabledata)

    for r in range(len(tabledata)):
        l_r_max = 0
        for c in range(len(tabledata[0])):
            if len(tabledata[r][c]) > l_r_max:
                l_r_max = len(tabledata[r][c])
        col_width[r] = l_r_max

    for column in range(len(tabledata[0])):
        for row in range(len(tabledata)):
            print(tabledata[row][column].rjust(col_width[row]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
print_table(tableData)
