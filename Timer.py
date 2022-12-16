import time as t
class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.time = 0

    def start(self):
        self.start_time = t.time()


    def stop(self):
        self.end_time = t.time()
        time = self.end_time - self.start_time
        self.time = time


    def __repr__(self):
        return f"{self.time:.2f}"