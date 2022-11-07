class Board:
    def __init__(self):
        self.placeHolder: str = "_"
        self.board: list[list[str]] = self.CreateBoard()

    def CreateBoard(self) -> list[list[str]]:

        emptyBoard: list[list[str]] = [
            [
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
            ],
            [
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
            ],
            [
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
            ],
            [
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
            ],
            [
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
            ],
            [
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
                self.placeHolder,
            ],
            ["1", "2", "3", "4", "5", "6", "7"],
        ]

        return emptyBoard

    def ShowBoard(self) -> None:
        for line in self.board:
            for element in line:
                print(f"|{element}", end="")
            print("|")

    def IsValidTurn(self, element: int) -> bool:
        element -= 1
        for line in range(len(self.board)):
            fieldIsFree = self.board[line][element] != self.placeHolder
            fieldIsValid = self.board[line - 1][element] == self.placeHolder
            if fieldIsFree and fieldIsValid:
                return True
        return False

    def AddCoinToBoard(self, element: int, playerSymbol: str):
        element -= 1
        for line in range(len(self.board)):
            fieldIsFree = self.board[line][element] != self.placeHolder
            fieldIsValid = self.board[line - 1][element] == self.placeHolder
            if fieldIsFree and fieldIsValid:
                self.board[line - 1][element] = playerSymbol
