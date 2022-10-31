from Board import Board
from Player import Player


class MainGame:
    def __init__(self):
        self.playerOne: Player = Player()
        self.playerTwo: Player = Player()
        self.board: Board = Board()
        self.roundNumber = 0

    def PrepareGame(self) -> None:
        self.playerOne.name = self.GetUserName("Spieler 1")
        self.playerOne.symbol = "X"
        self.playerTwo.name = self.GetUserName("Spieler 2")
        self.playerTwo.symbol = "O"

    def Turn(self, player: Player) -> None:
        self.board.ShowBoard()

        while True:
            row: int = self.GetRowInput(player.name)

            isvalidTurn: bool = self.board.IsValidTurn(row)

            if isvalidTurn:
                self.board.AddCoinToBoard(row, player.symbol)
                return
            else:
                print(
                    f"Du kannst deinen Stein nicht in Spalte '{row}' setzen. Versuch es nochmal!"
                )

    def Round(self) -> None:
        self.roundNumber += 1
        print(f"Round: {self.roundNumber}")
        self.Turn(self.playerOne)
        self.Turn(self.playerTwo)

    def Play(self) -> None:
        while True:
            self.Round()

    def GetUserName(self, playerName: str) -> str:
        while True:
            userName: str = input(f"{playerName}: Bitte gebe deinen Namen ein: ")

            inputIsValid: bool = userName.isalpha() and len(userName) > 0
            if inputIsValid:
                return userName
            else:
                print(f"Deine Eingabe'{userName}' ist ungültig. Versuch es nochmal!")

    def GetRowInput(self, playerName) -> int:
        while True:
            rowInputString: str = input(
                f"{playerName}: Wähle eine Spalte um deinen Stein zu setzen: "
            )

            try:
                rowInput = int(rowInputString)
                firstLine: int = 1
                lastLine: int = 7

                inputIsValid = firstLine <= rowInput <= lastLine
                if inputIsValid:
                    return rowInput
                else:
                    print(
                        f"Deine Eingabe '{rowInput}' ist ungültig. Versuch es nochmal"
                    )
            except ValueError:
                print("Bitte gebe eine Zahl ein")
