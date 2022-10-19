from Board import Board
from Player import Player
from StatusValidator import StatusValidator


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

    def Turn(self, player: Player) -> None or Player:
        self.board.ShowBoard()

        while True:
            row: int = self.GetRowInput(player.name)

            isvalidTurn: bool = self.board.IsValidTurn(row)

            if isvalidTurn:
                self.board.AddCoinToBoard(row, player.symbol)
                playerWins = StatusValidator.isWin(self.board, player, row)

                if playerWins:
                    return player
                break

            else:
                print(
                    f"Du kannst deinen Stein nicht in Spalte '{row}' setzen. Versuch es nochmal!")

    def Round(self) -> None or Player:
        winner: Player
        self.roundNumber += 1
        if self.roundNumber > 21:
            return Player()
        print(f"Round: {self.roundNumber}")
        winner = self.Turn(self.playerOne)
        if winner is None:
            winner = self.Turn(self.playerTwo)

        if winner is not None:
            return winner

    def Play(self) -> None:
        winner: Player
        while True:
            winner = self.Round()

            if winner is not None:
                break
        if winner.name == None:
            print("Unentschieden")
        else:
            print(f"{winner.name} hat gewonnen!")

    def GetUserName(self, playerName: str) -> str:
        while True:
            userName: str = input(
                f"{playerName}: Bitte gebe deinen Namen ein: ")

            inputIsValid: bool = userName.isalpha() and len(userName) > 0
            if inputIsValid:
                return userName
            else:
                print(
                    f"Deine Eingabe'{userName}' ist ungültig. Versuch es nochmal!")

    def GetRowInput(self, playerName: str) -> int:
        while True:
            rowInputString: str = input(
                f"{playerName}: Wähle eine Spalte um deinen Stein zu setzen: ")

            try:
                rowInput = int(rowInputString)
                firstLine: int = 1
                lastLine: int = 7

                inputIsValid = firstLine <= rowInput <= lastLine
                if inputIsValid:
                    return rowInput
                else:
                    print(
                        f"Deine Eingabe '{rowInput}' ist ungültig. Versuch es nochmal")
            except ValueError:
                print('Bitte gebe eine Zahl ein')
