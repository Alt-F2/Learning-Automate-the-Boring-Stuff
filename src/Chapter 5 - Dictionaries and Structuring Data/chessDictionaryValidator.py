import sys
from operator import truediv

chessBoard = {
    '8a':'', '8b':'', '8c':'', '8d':'', '8e':'', '8f':'', '8g':'', '8h':'',
    '7a':'', '7b':'', '7c':'', '7d':'', '7e':'', '7f':'', '7g':'', '7h':'',
    '6a':'', '6b':'', '6c':'', '6d':'', '6e':'', '6f':'', '6g':'', '6h':'',
    '5a':'', '5b':'', '5c':'', '5d':'', '5e':'', '5f':'', '5g':'', '5h':'',
    '4a':'', '4b':'', '4c':'', '4d':'', '4e':'', '4f':'', '4g':'', '4h':'',
    '3a':'', '3b':'', '3c':'', '3d':'', '3e':'', '3f':'', '3g':'', '3h':'',
    '2a':'', '2b':'', '2c':'', '2d':'', '2e':'', '2f':'', '2g':'', '2h':'',
    '1a':'', '1b':'', '1c':'', '1d':'', '1e':'', '1f':'', '1g':'', '1h':'' }

player1Pieces = {
    'wpawn': 1,
    'wknight': 1, 'wbishop': 1, 'wrook': 1,
    'wqueen': 1, 'wking': 1
}

player2Pieces = {
    'bpawn': 1,
    'bknight': 1, 'bbishop': 1, 'brook': 1,
    'bqueen': 1, 'bking': 1
}

stdPieces = {
    'wpawn': 8,
    'wknight': 2, 'wbishop': 2, 'wrook': 2,
    'wqueen': 1, 'wking': 1,
    'bpawn': 8,
    'bknight': 2, 'bbishop': 2, 'brook': 2,
    'bqueen': 1, 'bking': 1
}

def isValidChessBoard(board, piece) -> bool:
    total = sum(1 for v in board.values() if v == piece)
    if total <= stdPieces.get(piece):
        print("--Board is valid--")
        return True
    else:
        print("--Board is invalid--")
        return False

try:
    # player 1 placement
    count = 0
    while count < 6:
        try:
            print("-Please place select a chess piece to place-")
            print('Selectable Pieces:')
            print(player1Pieces)
            piece = input('Player 1! select a piece to place:')

            if player1Pieces[piece] > 0:
                placement = input('Place a piece on the board:')
                if chessBoard[placement] == '':
                    chessBoard[placement] = piece
                    player1Pieces[piece] -= 1
                    count += 1
            else:
                raise KeyError

        except KeyError:
            print("Invalid piece or chessboard placement.")

    count = 0
    while count < 6:
        try:
            print("-Please place select a chess piece to place-")
            print('Selectable Pieces:')
            print(player2Pieces)
            piece = input('Player 2! select a piece to place:')

            if player2Pieces[piece] > 0:
                placement = input('Place a piece on the board:')
                if chessBoard[placement] == '':
                    chessBoard[placement] = piece
                    player2Pieces[piece] -= 1
                    count += 1
            else:
                raise KeyError

        except KeyError:
            print("Invalid piece or chessboard placement.")

    print(chessBoard)

    isValidChessBoard(chessBoard, 'wpawn')
    isValidChessBoard(chessBoard, 'wknight')
    isValidChessBoard(chessBoard, 'wbishop')
    isValidChessBoard(chessBoard, 'wrook')
    isValidChessBoard(chessBoard, 'wqueen')
    isValidChessBoard(chessBoard, 'wking')
    isValidChessBoard(chessBoard, 'wpawn')

    isValidChessBoard(chessBoard, 'bpawn')
    isValidChessBoard(chessBoard, 'bknight')
    isValidChessBoard(chessBoard, 'bbishop')
    isValidChessBoard(chessBoard, 'brook')
    isValidChessBoard(chessBoard, 'bqueen')
    isValidChessBoard(chessBoard, 'bking')
    isValidChessBoard(chessBoard, 'bpawn')

except KeyboardInterrupt:
    sys.exit()




