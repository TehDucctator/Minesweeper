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
        for space in board[row-1][index-1:index+2]:
          if space[0] == "B":
            count += 1

      # row below
      if row+1 != 8:
        for space in board[row+1][index-1:index+2]:
          if space[0] == "B":
            count += 1
      
      board[row][index][0] = count

def main():
  set_up(board)
  count_bomb(board)
  print_board(board)
  
if __name__ == "__main__":
  main()