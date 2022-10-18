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
