class Board:
    def __init__(self):
        self.board: list[list[str]] = self.CreateBoard()

    def CreateBoard(self) -> list[list[str]]:
        placeHolder = "_"

        emptyBoard: list[list[str]] = [
            [placeHolder, placeHolder, placeHolder, placeHolder,
                placeHolder, placeHolder, placeHolder],
            [placeHolder, placeHolder, placeHolder, placeHolder,
                placeHolder, placeHolder, placeHolder],
            [placeHolder, placeHolder, placeHolder, placeHolder,
                placeHolder, placeHolder, placeHolder],
            [placeHolder, placeHolder, placeHolder, placeHolder,
                placeHolder, placeHolder, placeHolder],
            [placeHolder, placeHolder, placeHolder, placeHolder,
                placeHolder, placeHolder, placeHolder],
            [placeHolder, placeHolder, placeHolder, placeHolder,
                placeHolder, placeHolder, placeHolder],
            ["1", "2", "3", "4", "5", "6", "7"]
        ]

        return emptyBoard

    def ShowBoard(self) -> None:
        for line in self.board:
            for element in line:
                print(f"|{element}", end='')
            print("|")
