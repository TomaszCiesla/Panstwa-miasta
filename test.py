import random


def generate_board(rows, cols, num_mines):
    board = [[0] * cols for _ in range(rows)]
    mine_positions = random.sample(range(rows * cols), num_mines)

    for position in mine_positions:
        row = position // cols
        col = position % cols
        board[row][col] = -1

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < rows and 0 <= c < cols and board[r][c] != -1:
                    board[r][c] += 1

    return board


def print_board(board, reveal=False):
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            if reveal or board[r][c] >= 0:
                print(str(board[r][c]) if board[r][c] >= 0 else '*', end=' ')
            else:
                print('.', end=' ')
        print()


def play_game():
    rows = 8
    cols = 8
    num_mines = 20
    board = generate_board(rows, cols, num_mines)
    revealed = [[False] * cols for _ in range(rows)]

    while True:
        print_board(revealed)
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))

        if board[row][col] == -1:
            print_board(board, reveal=True)
            print("Game Over!")
            break
        else:
            revealed[row][col] = True

            if all(revealed[r][c] or board[r][c] == -1 for r in range(rows) for c in range(cols)):
                print_board(board, reveal=True)
                print("You Win!")
                break


if __name__ == "__main__":
    play_game()
