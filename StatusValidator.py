from Board import Board
from Player import Player


class StatusValidator:
    def __init__(self):
        pass

    @classmethod
    def isWin(cls, board: Board, player: Player, column: int) -> bool:
        horizontalWin = cls.horizontalWin(board, player)
        verticalWin = cls.verticalWin(board, player, column)
        diagonalWin = cls.diagonalWin(board, player)

        return horizontalWin or verticalWin or diagonalWin

    @classmethod
    def horizontalWin(cls, board: Board, player: Player) -> bool:
        for row in board.board:
            if cls.winSequence(row, player):
                player.isWinner = True
                return True

        return False

    @classmethod
    def verticalWin(cls, board: Board, player: Player, column: int) -> bool:
        sequence = []
        column -= 1
        for row in range(len(board.board)):
            sequence.append(board.board[row][column])

        if cls.winSequence(sequence, player):
            player.isWinner = True
            return True

        return False

    @classmethod
    def diagonalWin(cls, board: Board, player: Player) -> bool:
        boardMatrix: list[list[str]] = board.board
        symbol: str = player.symbol
        columns: int = len(boardMatrix[0])
        rows: int = len(boardMatrix) - 1

        for column in range(columns - 3):
            for row in range(rows - 3):
                if (
                    boardMatrix[row][column] == symbol
                    and boardMatrix[row + 1][column + 1] == symbol
                    and boardMatrix[row + 2][column + 2] == symbol
                    and boardMatrix[row + 3][column + 3] == symbol
                ):
                    return True

        for column in range(columns - 3):
            for row in range(3, rows):
                if (
                    boardMatrix[row][column] == symbol
                    and boardMatrix[row - 1][column + 1] == symbol
                    and boardMatrix[row - 2][column + 2] == symbol
                    and boardMatrix[row - 3][column + 3] == symbol
                ):
                    player.isWinner = True
                    return True

        return False

    @classmethod
    def winSequence(cls, row: list[str], player: Player) -> bool:
        winnerSequence = player.symbol * 4
        sequenceString = str.join("", row)
        winSequece = winnerSequence in sequenceString

        return winSequece
