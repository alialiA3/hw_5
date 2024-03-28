from game import CammanGame

if __name__ == "__main__":
    player_name = input("Введите ваше имя: ")
    game = CammanGame(player_name)
    game.play()