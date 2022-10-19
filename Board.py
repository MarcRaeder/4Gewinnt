from typing import List


class Board:
    def __init__(self):
        self.placeHolder: str = "_"
        self.board: List[List[str]] = self.CreateBoard()

    def CreateBoard(self) -> List[List[str]]:

        emptyBoard: List[List[str]] = [
            [self.placeHolder, self.placeHolder, self.placeHolder, self.placeHolder,
                self.placeHolder, self.placeHolder, self.placeHolder],
            [self.placeHolder, self.placeHolder, self.placeHolder, self.placeHolder,
                self.placeHolder, self.placeHolder, self.placeHolder],
            [self.placeHolder, self.placeHolder, self.placeHolder, self.placeHolder,
                self.placeHolder, self.placeHolder, self.placeHolder],
            [self.placeHolder, self.placeHolder, self.placeHolder, self.placeHolder,
                self.placeHolder, self.placeHolder, self.placeHolder],
            [self.placeHolder, self.placeHolder, self.placeHolder, self.placeHolder,
                self.placeHolder, self.placeHolder, self.placeHolder],
            [self.placeHolder, self.placeHolder, self.placeHolder, self.placeHolder,
                self.placeHolder, self.placeHolder, self.placeHolder],
            ["1", "2", "3", "4", "5", "6", "7"]
        ]

        return emptyBoard

    def ShowBoard(self) -> None:
        for line in self.board:
            for element in line:
                print(f"|{element}", end='')
            print("|")

    def IsValidTurn(self, row: int) -> bool:
        row -= 1
        for index in range(len(self.board)):
            if self.board[index][row] != self.placeHolder:
                if self.board[index - 1][row] == self.placeHolder:
                    return True
        return False

    def AddCoinToBoard(self, row: int, playerSymbol: str):
        row -= 1
        for index in range(len(self.board)):
            if self.board[index][row] != self.placeHolder:
                if self.board[index - 1][row] == self.placeHolder:
                    self.board[index - 1][row] = playerSymbol
