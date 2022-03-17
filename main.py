import random

board = [[[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[]]]

# prints the board
def print_board(board: list):
  print("  1 2 3 4 5 6 7 8")
  row_count = 0
  for row in board:
    row_count += 1
    print(row_count, end=" ")
    for element in row:
      print(element[0], end=" ")

    print()


# sets up board
def set_up(board: list):
  for row in board:
    for element in row:
      rng = random.randint(1, 8)
      if rng == 8:
        element.append("B")
      else:
        element.append("?")
  
  count_bomb(board)


def count_bomb(board: list):
  for row in range(len(board)):
    for index in range(len(board)):
      count = 0

      if board[row][index][0] == "B": # skips if is bomb
        continue

      # same row
      if index+1 != 8:
        if board[row][index+1][0] == "B":
          count += 1
      if index-1 != -1:
        if board[row][index-1][0] == "B":
          count += 1

      # row above
      if row-1 != -1:
        for space in board[row-1][max(index-1, 0):index+2]:
          if space[0] == "B":
            count += 1

      # row below
      if row+1 != 8:
        for space in board[row+1][max(index-1, 0):index+2]:
          if space[0] == "B":
            count += 1
      
      board[row][index][0] = count


def hide_board(board: list):
  # copies board
  p_board = []
  for row in board:
    p_row = []
    for elem in row:
      p_row.append(elem[:])
    p_board.append(p_row)
  
  # replaces spaces on board with ?
  for ri, row in enumerate(p_board):
    for space_i in range(len(row)):
      p_board[ri][space_i][0] = "?"
  
  return p_board


def dig(p_board: list, board: list):
  row, column = input("Enter the space you want to dig (type the row number then the column number): ").split()
  ri = int(row) - 1
  ci = int(column) - 1
  spot = board[ri][ci][:]

  p_board[ri][ci] = spot

  print_board(p_board)
  return spot[0]


def game(p_board: list, board: list):
  alive = True

  while alive:
    if dig(p_board, board) == "B":
      alive = False
      print("Game Over")


def main():
  set_up(board)
  p_board = hide_board(board)
  print_board(board)
  print_board(p_board)
  game(p_board, board)
  
if __name__ == "__main__":
  main()