board = ['...', '...', '...']

temp = list(board[0])
temp[1] = 'x'
board[0] = ''.join(temp)

print(board)