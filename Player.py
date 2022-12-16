class Player:
    def __init__(self, name, score = 0, time = 0):
        self.__name = name
        self.__score = score
        self.__time = time

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 12:
            print("Player's name cannot more then 12 characters")
        else:
            self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time
