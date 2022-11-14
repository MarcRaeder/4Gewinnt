from typing import Optional
from Board import Board
from Player import Player
from StatusValidator import StatusValidator

MAXROUNDS: int = 21


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

    def Turn(self, player: Player) -> Optional[Player]:
        self.board.ShowBoard()

        while True:
            row: int = self.GetRowInput(player.name)

            isValidTurn: bool = self.board.IsValidTurn(row)

            if isValidTurn:
                self.board.AddCoinToBoard(row, player.symbol)

                playerWins = StatusValidator.isWin(self.board, player, row)

                if playerWins:
                    return player
                return player

            else:
                print(
                    f"Du kannst deinen Stein nicht in Spalte '{row}' setzen. Versuch es nochmal!"
                )

                return player

    def Round(self) -> Optional[Player]:
        self.roundNumber += 1
        if self.roundNumber > MAXROUNDS:
            return Player()
        print(f"Round: {self.roundNumber}")
        winner: Player = self.Turn(self.playerOne)
        if not winner.isWinner:
            winner = self.Turn(self.playerTwo)

        if winner.isWinner:
            return winner

    def Play(self) -> None:
        winner: Player
        while True:
            winner = self.Round()

            if winner is not None:
                break
        if winner.name == "":
            print("Unentschieden")
        else:
            print(f"{winner.name} hat gewonnen!")

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
