import Timer, Player, Scoreboard
class Game:
    def __init__(self, deck_dict, option=0, mode=0):
        self.__option = option
        self.__mode = mode
        self.__deck_dict = deck_dict

    @property
    def option(self):
        return self.__option

    @option.setter
    def option_select(self, option):
        self.__option = option

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode_select(self, mode):
        self.__mode = mode

    def bonus_reset(self):
        self.__bonus = True


    def start(self):
        print("|===========================================================================================================================================|")
        print("|                                                               Mat[c]hed                                                                   |")
        print("1. Start                                                                                                                                    |")
        print("2. Scoreboard                                                                                                                               |")
        print("3. Quit                                                                                                                                     |")
        print("|===========================================================================================================================================|")


    def choice1(self):
        print("|===========================================================================================================================================|")
        print("1. Singleplayer                                                                                                                             |")
        print("2. Two - player                                                                                                                             |")
        print("3. Back                                                                                                                                     |")


    def board(self):
        line = 0
        for i in self.__deck_dict.values():
            if line%6 == 0:
                print()
            print(i, end ="    ")
            line +=1
        print()


    def card_select(self):
        while True:
            try:
                num = int(input("Select your card: "))
                self.__deck_dict[num].flip()
                print("|===========================================================================================================================================|")
            except KeyError:
                print("Please input valid number")
                continue
            except ValueError:
                print("Input must be an number")
                continue
            else:
                if self.__deck_dict[num].position == 0:
                    print("The card already matched")
                    continue
                break
        return num
    def twoplayer(self, game):
        print("|==============================================================Two - player=================================================================|")
        player1 = input("Enter player 1 name: ")
        player2 = input("Enter player 2 name: ")
        self.__player1 = Player.Player(name=player1)
        self.__player2 = Player.Player(name=player2)
        count = 0
        turn = 1
        bonus = Timer.Timer()
        while True:
            bonus.time = 0
            game.info_for_two()
            game.board()
            if turn == 1:
                print(f"{self.__player1.name}'s turn")
                bonus.start()
                first = game.card_select()
                game.info_for_two()
                game.board()
                while True:
                    second = game.card_select()
                    if second == first:
                        self.__deck_dict[second].flip()
                        print("Second card cannot be the same as First card")
                        continue
                    break
                bonus.stop()
                if bonus.time > 10:
                    print("Turn skips")
                    turn += 1
                    continue
                game.info_for_two()
                game.board()
                Timer.t.sleep(3)
                print("|===========================================================================================================================================|")
                if self.__deck_dict[first].is_match(self.__deck_dict[second]):
                    self.__deck_dict[first].matched()
                    self.__deck_dict[second].matched()
                    self.__player1.score += self.__deck_dict[first].card['difficulty'] + self.__deck_dict[second].card['difficulty']
                    if bonus.time <= 3:
                        self.__player1.score += 1
                    count += 1
                    print(bonus.time)
                    continue
                else:
                    self.__deck_dict[first].flip()
                    self.__deck_dict[second].flip()
                turn += 1
            elif turn == 2:
                print(f"{self.__player2.name}'s turn")
                bonus.start()
                first = game.card_select()
                game.info_for_two()
                game.board()
                while True:
                    second = game.card_select()
                    if second == first:
                        self.__deck_dict[second].flip()
                        print("Second card cannot be the same as First card")
                        continue
                    break
                bonus.stop()
                if bonus.time > 10:
                    print("Turn skips")
                    turn -= 1
                    continue
                game.info_for_two()
                game.board()
                Timer.t.sleep(3)
                print("|===========================================================================================================================================|")
                if self.__deck_dict[first].is_match(self.__deck_dict[second]):
                    self.__deck_dict[first].matched()
                    self.__deck_dict[second].matched()
                    self.__player2.score += self.__deck_dict[first].card['difficulty'] + self.__deck_dict[second].card['difficulty']
                    if bonus.time <= 3:
                        self.__player2.score += 1
                    count += 1
                    print(f"time: {time.bonus.time:.2f}")
                    continue
                else:
                    self.__deck_dict[first].flip()
                    self.__deck_dict[second].flip()
                turn -= 1
            if count == 15:
                break
        if self.__player1.score > self.__player2.score:
                print(f"{self.__player1.name} wins")
        elif self.__player1.score < self.__player2.score:
                print(f"{self.__player2.name} wins")
        else:
            print("TIE")

    def info_for_two(self):
        print(f"{self.__player1.name}'s score: {self.__player1.score}")
        print(f"{self.__player2.name}'s score: {self.__player2.score}")


    def info_for_single(self, timer):
        self.__player.time += timer.time
        print(f"Name: {self.__player.name}                                                                                                                        Time: {self.__player.time:.2f}")
        print(f"Score: {self.__player.score}")


    def singleplayer(self, game):
        timer = Timer.Timer()
        print("|===============================================================Singleplayer================================================================|")
        name = input("Enter your name: ")
        self.__player = Player.Player(name)
        count = 0
        while True:
            game.info_for_single(timer)
            game.board()
            timer.start()
            first = game.card_select()
            timer.stop()
            game.info_for_single(timer)
            game.board()
            while True:
                timer.start()
                second = game.card_select()
                if second == first:
                    self.__deck_dict[second].flip()
                    print("Second card cannot be the same as First card")
                    continue
                break
            timer.stop()
            game.info_for_single(timer)
            game.board()
            Timer.t.sleep(3)
            print("|===========================================================================================================================================|")

            if self.__deck_dict[first].is_match(self.__deck_dict[second]):
                self.__deck_dict[first].matched()
                self.__deck_dict[second].matched()
                self.__player.score += self.__deck_dict[first].card['difficulty'] + self.__deck_dict[second].card['difficulty']
                count += 1
            else:
                self.__deck_dict[first].flip()
                self.__deck_dict[second].flip()
            if count == 15:
                break
        print("|Congratulations ")
        print(f"|You win with a time of {self.__player.time:.2f} seconds")
        scorebaord = Scoreboard.Scoreboard("scoreboard.json")
        scorebaord.update_score(self.__player.name, self.__player.time)







