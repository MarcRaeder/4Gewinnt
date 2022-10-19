import math

from Board import Board
from Player import Player


class MainGame:
    def __init__(self):
        self.playerOne: Player = Player()
        self.playerTwo: Player = Player()
        self.board: Board = Board()
        self.roundNumber = 0

    def PrepareGame(self) -> None:
        self.playerOne.name = self.GetUserName("Player 1")
        self.playerOne.symbol = "X"
        self.playerTwo.name = self.GetUserName("Player 2")
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
                    f"You can't put a coin into row '{row}'. Please try again")

    def Round(self) -> None:
        self.roundNumber += 1
        print(f"Round: {math.ceil(self.roundNumber / 2)}")
        if self.roundNumber % 2 != 0:
            self.Turn(self.playerOne)
        else:
            self.Turn(self.playerTwo)

    def Play(self) -> None:
        while True:
            self.Round()

    def GetUserName(self, greeting: str) -> str:
        while True:
            userName: str = input(f"{greeting}: Please enter your name: ")

            inputIsValid: bool = userName.isalpha() and len(userName) > 0
            if inputIsValid:
                return userName
            else:
                print(
                    f"Your input '{userName}' is not valid. Please try again")

    def GetRowInput(self, playerName: str) -> int:
        while True:
            rowInputString: str = input(
                f"{playerName}: Select a row to put your coin: ")

            try:
                rowInput = int(rowInputString)

                inputIsValid = 1 <= rowInput <= 7
                if inputIsValid:
                    return rowInput
                else:
                    print(
                        f"Your input '{rowInput}' is not valid. Please try again")
            except ValueError:
                print('Please enter an integer')
