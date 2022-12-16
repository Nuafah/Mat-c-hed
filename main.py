import Card
import Game
import Scoreboard
import json

with open("card_data.json", "r") as datafile:
    data = json.load(datafile)

card_1 = Card.Card(data['card1'])
card_2 = Card.Card(data['card2'])
card_3 = Card.Card(data['card3'])
card_4 = Card.Card(data['card4'])
card_5 = Card.Card(data['card5'])
card_6 = Card.Card(data['card6'])
card_7 = Card.Card(data['card7'])
card_8 = Card.Card(data['card8'])
card_9 = Card.Card(data['card9'])
card_10 = Card.Card(data['card10'])
card_11 = Card.Card(data['card11'])
card_12 = Card.Card(data['card12'])
card_13 = Card.Card(data['card13'])
card_14 = Card.Card(data['card14'])
card_15 = Card.Card(data['card15'])
card_16 = Card.Card(data['card16'])
card_17 = Card.Card(data['card17'])
card_18 = Card.Card(data['card18'])
card_19 = Card.Card(data['card19'])
card_20 = Card.Card(data['card20'])
card_21 = Card.Card(data['card21'])
card_22 = Card.Card(data['card22'])
card_23 = Card.Card(data['card23'])
card_24 = Card.Card(data['card24'])
card_25 = Card.Card(data['card25'])
card_26 = Card.Card(data['card26'])
card_27 = Card.Card(data['card27'])
card_28 = Card.Card(data['card28'])
card_29 = Card.Card(data['card29'])
card_30 = Card.Card(data['card30'])

deck = [card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_11, card_12, card_13,
        card_14, card_15, card_16, card_17, card_18, card_19, card_20, card_21, card_22, card_23, card_24, card_25,
        card_26, card_27, card_28, card_29, card_30]
num_lst = []
for i in deck:
    while True:
        i.random_position()
        if i.position not in num_lst:
            num_lst.append(i.position)
            break
deck_dict = {}
for i in deck:
    deck_dict.update({i.position: i})
deck_dict = dict(sorted(deck_dict.items()))
while True:
    scoreboard = Scoreboard.Scoreboard("scoreboard.json")
    game = Game.Game(deck_dict)
    game.start()
    try:
        choice = int(input("Please select: "))
        if choice not in range(1, 4):
            print("Please select 1 - 3")
            continue
    except ValueError:
        print("Please select 1 - 3")
        continue
    else:
        pass
    game.option_select = choice
    if game.option == 1:
        game.choice1()
        while True:
            try:
                mode = int(input("select your gamemode: "))
            except ValueError:
                print("Please select 1 - 3")
                continue
            else:
                break
        game.mode_select = mode
        if mode == 1:
            game.singleplayer(game)
        elif mode == 2:
            game.twoplayer(game)
        elif mode == 3:
            continue
        continue
    elif game.option == 2:
        scoreboard.get_top_scores()
        back = input("Enter to back: ")
        if back == "":
            continue
    elif game.option == 3:
        break
