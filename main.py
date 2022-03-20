import random

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


# sets up board, returns board with bombs placed
def set_up():
  board = [[[],[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[],[]]]

  for row in board:
    for element in row:
      rng = random.randint(1, 8)
      if rng == 8:
        element.append("B")
      else:
        element.append("?")
  
  count_bomb(board)
  return board

# counts bombs around a space and writes to the board
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

# digs at space given, returns what was dug, returns None if out of range or placing flag
def dig(p_board: list, board: list, row: int, column: int, d: str):
  ri = int(row) - 1
  ci = int(column) - 1
  try:
    spot = board[ri][ci][:]
  except IndexError:
    return None

  if d == "d":
    p_board[ri][ci] = spot
    return spot[0]
    
  elif d == "f":
    p_board[ri][ci][0] = "F"

  return None
  
# checks if won
def check(p_board, board):
  won = True

  for row in range(len(p_board)):
    for elem in range(len(p_board[row])):
      if p_board[row][elem][0] == board[row][elem][0]:
        continue

      elif p_board[row][elem][0] == "F":

        if board[row][elem][0] == "B":
          continue

        else:
          won = False

      else:
        won = False


  return won

# main game loop
def game(p_board: list, board: list):
  alive = True

  while alive:
    print_board(p_board)
    try:
      row, column, d = input("Enter the space you want to dig \n(type the row number then the column number, then d or f to dig or place a flag):\n").split()
      
      try:
        row = int(row)
        column = int(column)

      except ValueError:
        continue

    except ValueError:
      continue

    if dig(p_board, board, row, column, d) == "B": # dug bomb
      print_board(board)
      alive = False
      print("Game Over")
    elif check(p_board, board): # won
      alive = False
      print("You Won!")

# main function
def main():
  board = set_up()
  p_board = hide_board(board)
  game(p_board, board)
  
if __name__ == "__main__":
  main()