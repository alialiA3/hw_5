from comman import Camman
class CammanGame:
    def __init__(self, player_name) -> None:
        self.player_name = player_name
        self.comman = Camman()
        self.player_score = 0
    

    def play(self):
        print(f"Добро пожалавать в игру Лохотрон , {self.player_name}")
        print("Угадайте где находится шарик!")
        print("1.Левая рука")
        print("2.Правая рука")
        print("3.Карман")
        choise = int(input("Выберите 1, 2 или 3: "))


        if self.comman.check_choise(choise):
            print("Поздровляем! Вы угадали")
            self.player_score += 1
        else:
            print("К сажелению вы не угадали")
            print(f"Шарик находится в {self.comman.ball_position}")

        print(f"Ваш счет: {self.player_score}")
        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again == "да":
            self.play()
        else:
            print("Спасибо за игру!")            