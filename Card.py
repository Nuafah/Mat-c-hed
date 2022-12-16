class Card:
    def __init__(self, card, position = 0, face = 'down', difficulty=0):
        self.__position = position
        self.__difficulty = difficulty
        self.__face = face
        self.__card = card

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self,position):
        self.__position = position

    @property
    def face(self):
        return self.__face
    @property
    def card(self):
        return self.__card

    def flip(self): #use to flip a card
        if self.__face == 'down':
            self.__face = 'up'
        elif self.__face == 'up':
            self.__face = 'down'

    def is_match(self, other): #to check if the card match with other
        return self.__card['answer'] == other.card['answer']

    def matched(self): #when the card matched remove card from display
        self.__position = 0

    def random_position(self):
        import random
        position = random.randint(1, 30)
        self.__position = position


    def __str__(self):
        if self.__position == 0:
            return "                    "
        if self.__face == 'down':
            if self.__position < 10:
                return f"{self.__position}:##################"
            return f"{self.__position}:#################"
        elif self.__face == 'up':
            x = f"{self.__position}:{self.__card['equation']}"
            while len(x) < 20:
                x += " "
            return x
