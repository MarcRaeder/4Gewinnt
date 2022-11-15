from MainGame import MainGame


def main() -> None:
    playAgain = "JA"

    while playAgain.upper() == "JA":
        game = MainGame()

        game.PrepareGame()
        game.Play()

        playAgain = input(
            "Möchtest Ihr noch eine Runde spielen? Dann bestätige mit JA: "
        )

    print("Auf Wiedersehen!")


if __name__ == "__main__":
    main()
