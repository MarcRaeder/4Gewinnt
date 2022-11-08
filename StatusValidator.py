from Board import Board
from Player import Player


class StatusValidator:
    def __init__(self):
        pass

    def isWin(board: Board, player: Player, column: int) -> bool:
        horizontalWin = StatusValidator.horizontalWin(board, player)
        verticalWin = StatusValidator.verticalWin(board, player, column)
        diagonalWin = StatusValidator.diagonalWin(board, player)

        return horizontalWin or verticalWin or diagonalWin

    def horizontalWin(board: Board, player: Player) -> bool:
        for row in board.board:
            if StatusValidator.winSequence(row, player):
                return True

        return False

    def verticalWin(board: Board, player: Player, column: int) -> bool:
        sequence = []
        column -= 1
        for row in range(len(board.board)):
            sequence.append(board.board[row][column])

        if StatusValidator.winSequence(sequence, player):
            return True

        return False

    def diagonalWin(board: Board, player: Player) -> bool:
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
                    return True

        return False

    def winSequence(row: list[str], player: Player) -> bool:
        winnerSequence = player.symbol * 4
        sequenceString = str.join("", row)
        winSequece = winnerSequence in sequenceString

        return winSequece
