def print_board(board):
    for i, row in enumerate(board):
        row_str = ""
        for j, value in enumerate(row):
            row_str += value
            if j != len(row)-1:
                row_str += " | "

        print(row_str)
        if i != len(board)-1:
            print("----------")


board = [
    ["x", " ", " "],
    [" ", "o", " "],
    [" ", " ", "x"],
]

print_board(board)
