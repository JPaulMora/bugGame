from functools import reduce
from operator import add


board = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

def flatten(b):
  return reduce(add ,b)


def possibleMoves(pastMoves, x, y):
  possible = []
  if x > 0 and board[y][x-1] not in pastMoves:
    possible.append([y,x -1])

  if x < 3 and board[y][x+1] not in pastMoves:
    possible.append([y,x+1]) 

  if y > 0 and board[y-1][x] not in pastMoves:
    possible.append([y-1,x])

  if y < 3 and board[y+1][x] not in pastMoves:
    possible.append([y+1,x])

  return possible

def solve(pm, y, x):
  moves = possibleMoves(pm, x, y)
  if len(moves) != 0:
    pm2 = pm.copy()
    if pm == [] and board[y][x] == 1:
      pass
    else:
      pm2.append(board[y][x])
      
    for move in moves:
      solve(pm2, move[0], move[1])

  elif sorted(pm) == answer and board[y][x] == 16:
    print(pm)
    print("solved!")

  else:
    pass
    
solve([], 0,0)
