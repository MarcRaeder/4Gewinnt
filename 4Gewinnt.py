from MainGame import MainGame


def main() -> None:
    playagain = "JA"

    while playagain.upper() == "JA":
        game = MainGame()

        game.PrepareGame()
        game.Play()

        playagain = input(
            "Möchtest Ihr noch eine Runde spielen? Dann bestätige mit JA: ")

    print("Auf Wiedersehen!")


if __name__ == '__main__':
    main()
