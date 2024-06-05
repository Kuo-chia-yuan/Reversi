def create():
  list1 = [['.' for i in range(8)] for j in range(8)]
  list1[3][3] = 'O'
  list1[3][4] = 'X'
  list1[4][3] = 'X'
  list1[4][4] = 'O'
  return list1

def see(board):
  print('  0 1 2 3 4 5 6 7')
  for i in range(8):
    print(i, end = ' ')
    for j in range(8):
      print(board[i][j], end = ' ')
    print()
  print('-----------------')

def player1(board):
  row = int(input('行：'))
  col = int(input('列：'))
  board[row][col] = 'O'
  return row, col

def player2(board):
  row = int(input('行：'))
  col = int(input('列：'))
  board[row][col] = 'X' 
  return row, col

def check(board, row, col, me, enemy):
  # 往上補齊
  flag = False
  if row>0:
    for i in range(row-1, -1, -1):
      if board[i][col]==me:
        flag = True
        break
    if flag==True:
      for i in range(row-1, -1, -1):
        if board[i][col]==enemy:
          board[i][col]=me
        else:
          break
  # 往下補齊
  flag = False
  if row<7:
    for i in range(row+1, 8, 1):
      if board[i][col]==me:
        flag = True
        break
    if flag==True:
      for i in range(row+1, 8, 1):
        if board[i][col]==enemy:
          board[i][col]=me
        else:
          break
  # 往右補齊
  flag = False
  if col<7:
    for i in range(col+1, 8, 1):
      if board[row][i]==me:
        flag = True
        break
    if flag==True:
      for i in range(col+1, 8, 1):
        if board[row][i]==enemy:
          board[row][i]=me
        else:
          break  
  # 往左補齊
  flag = False
  if col>0:
    for i in range(col-1, -1, -1):
      if board[row][i]==me:
        flag = True
        break
    if flag==True:
      for i in range(col-1, -1, -1):
        if board[row][i]==enemy:
          board[row][i]=me
        else:
          break
  # 往右下補齊
  flag = False
  if col<7 and row<7:
    i = 1
    while row+i<8 and col+i<8:
      if board[row+i][col+i]==me:
        flag = True
        break
      i += 1
    if flag==True:
      i = 1
      while row+i<8 and col+i<8:
        if board[row+i][col+i]==enemy:
          board[row+i][col+i]=me
          i += 1
        else:
          break
  # 往左上補齊
  flag = False
  if col>0 and row>0:
    i = 1
    while row-i>=0 and col-i>=0:
      if board[row-i][col-i]==me:
        flag = True
        break
      i += 1
    if flag==True:
      i = 1
      while row-i>=0 and col-i>=0:
        if board[row-i][col-i]==enemy:
          board[row-i][col-i]=me
          i += 1
        else:
          break
  # 往右上補齊
  flag = False
  if col<7 and row>0:
    i = 1
    while row-i>=0 and col+i<8:
      if board[row-i][col+i]==me:
        flag = True
        break
      i += 1
    if flag==True:
      i = 1
      while row-i>=0 and col+i<8:
        if board[row-i][col+i]==enemy:
          board[row-i][col+i]=me
          i += 1
        else:
          break
  # 往左下補齊
  flag = False
  if col>0 and row<7:
    i = 1
    while row+i<8 and col-i>=0:
      if board[row+i][col-i]==me:
        flag = True
        break
      i += 1
    if flag==True:
      i = 1
      while row+i<8 and col-i>=0:
        if board[row+i][col-i]==enemy:
          board[row+i][col-i]=me
          i += 1
        else:
          break


def win_loss(board):
  empty = [[i, j] for i in range(8) for j in range(8) if board[i][j] == '.']
  if empty==[]:    
    player1 = 0
    player2 = 0
    for i in range(8):
      for j in range(8):
        if board[i][j]=='O':
          player1 += 1
        elif board[i][j]=='X':
          player2 += 1
    if player1 > player2:
      print('player1 win')
    elif player1 < player2:
      print('player2 win')
    else:
      print('even')
    return True
  else:
    return False

def main():
  list1 = create()
  see(list1)

  while True:
    row, col = player1(list1)
    check(list1, row, col, 'O', 'X')
    see(list1)
    if win_loss(list1):
      break

    row, col = player2(list1)
    check(list1, row, col, 'X', 'O')
    see(list1)
    if win_loss(list1):
      break

main()