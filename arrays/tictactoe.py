"""
check the validity of a tic-tac-toe board
"""

winpositions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def isWin(board, c):
	for i in range(8):
		if board[winpositions[i][0]] == c and \
		board[winpositions[i][1]] == c and \
		board[winpositions[i][2]] == c:
			return True
	return False


def isValid(board):
	xc, oc = 0, 0

	# get the count of x's and o's
	for i in range(9):
		if board[i] == 'X':
			xc += 1
		if board[i] == 'O':
			oc += 1

	if xc == oc or xc == oc + 1:

		# O wins
		if isWin(board, 'O'):
			if isWin(board, 'X'):
				return False
			return xc == oc

		# X wins
		if isWin(board, 'X') and xc != oc + 1:
			return False

		return True

	return False

if __name__ == '__main__':
	board = ['X', 'X', 'O', 'O', 'X', 'X', ' ', ' ', ' ']
	print (isValid(board))



