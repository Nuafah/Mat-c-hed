import json

class Scoreboard:
    def __init__(self, filename):
        self.filename = filename
        self.scores = []
        self.load_scores()

    def load_scores(self):
        try:
            with open(self.filename, "r") as f:
                self.scores = json.load(f)
        except (FileNotFoundError, ValueError):
            self.scores = []

    def save_scores(self):
        with open(self.filename, "w") as f:
            json.dump(self.scores, f)

    def add_score(self, player, score):
        self.scores.append({"player": player, "score": score})
        self.scores.sort(key=self.sort_scores)
        self.save_scores()

    def update_score(self, player, score):
        for i in self.scores:
            if i["player"] == player:
                if score < i["score"]:
                    i["score"] = score
                    self.scores.sort(key=self.sort_scores)
                    self.save_scores()
        self.add_score(player, score)

    def sort_scores(self, score):
        return score["score"]

    def get_top_scores(self, num_scores=10):
        top = self.scores[:num_scores]
        print("|============================================================= Scoreboard ==================================================================|")
        for i in range(len(top)):
            print(f'{i+1}.{top[i]["player"]} : {top[i]["score"]:.2f}')