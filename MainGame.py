from Player import Player
from Board import Board


class MainGame:
    def __init__(self):
        self.playerOne: Player = Player()
        self.playerTwo: Player = Player()
        self.board: Board = Board()

    def PrepareGame(self) -> None:
        self.playerOne.name = self.GetUserName("Player 1")
        self.playerOne.symbol = "X"
        self.playerTwo.name = self.GetUserName("Player 2")
        self.playerTwo.symbol = "O"

    def GetUserName(self, greeting: str) -> str:
        while True:
            userName: str = input(f"{greeting}: Please enter your name: ")

            inputIsValid: bool = userName.isalpha() and len(userName) > 0
            if inputIsValid:
                return userName
            else:
                print(
                    f"Your input '{userName}' is not valid. Please try again")

    def Turn(self, playerName) -> None:
        row: int = self.GetRowInput(playerName)

    def GetRowInput(self, playerName) -> int:
        while True:
            try:
                rowInputString: str = input(
                    f"{playerName}: Select a row to put your coin:")
                rowInput = int(rowInputString)

                return rowInput
            except ValueError:
                print("Your Value is invalid. Try again!")

    def Round(self) -> None:
        playerName: str = self.playerOne.name
        self.Turn(playerName)
        playerName = self.playerTwo.name
        self.Turn(playerName)

    def Play(self) -> None:
        round: int = 0

        while True:
            print(f"Round: {round}")
            self.board.ShowBoard()
            self.Round()
            round += 1
