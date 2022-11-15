from Board import Board


class StatusValidator:
    def __init__(self):
        pass

    @classmethod
    def isWin(cls, board: Board, playerSymbol: str, column: int) -> bool:
        horizontalWin = cls.horizontalWin(board, playerSymbol)
        verticalWin = cls.verticalWin(board, playerSymbol, column)
        diagonalWin = cls.diagonalWin(board, playerSymbol)

        return horizontalWin or verticalWin or diagonalWin

    @classmethod
    def horizontalWin(cls, board: Board, playerSymbol: str) -> bool:
        for row in board.board:
            if cls.winSequence(row, playerSymbol):

                return True

        return False

    @classmethod
    def verticalWin(cls, board: Board, playerSymbol: str, column: int) -> bool:
        sequence = []
        column -= 1
        for row in range(len(board.board)):
            sequence.append(board.board[row][column])
        if cls.winSequence(sequence, playerSymbol):
            return True

        return False

    @classmethod
    def diagonalWin(cls, board: Board, playerSymbol: str) -> bool:
        boardMatrix: list[list[str]] = board.board
        columns: int = len(boardMatrix[0])
        rows: int = len(boardMatrix) - 1

        for column in range(columns - 3):
            for row in range(rows - 3):
                if (
                    boardMatrix[row][column] == playerSymbol
                    and boardMatrix[row + 1][column + 1] == playerSymbol
                    and boardMatrix[row + 2][column + 2] == playerSymbol
                    and boardMatrix[row + 3][column + 3] == playerSymbol
                ):
                    return True

        for column in range(columns - 3):
            for row in range(3, rows):
                if (
                    boardMatrix[row][column] == playerSymbol
                    and boardMatrix[row - 1][column + 1] == playerSymbol
                    and boardMatrix[row - 2][column + 2] == playerSymbol
                    and boardMatrix[row - 3][column + 3] == playerSymbol
                ):

                    return True

        return False

    @classmethod
    def winSequence(cls, row: list[str], playerSymbol: str) -> bool:
        winnerSequence = playerSymbol * 4
        sequenceString = str.join("", row)
        winSequece = winnerSequence in sequenceString

        return winSequece
