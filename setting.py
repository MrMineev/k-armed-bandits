import random
from numpy import random as nrandom

class Bandits:
    STDDIVIATION =5
    REWARD_SIZE = 5

    def __init__(self, k=10):
        self.k = k
        self.distributions = []

        for i in range(self.k):
            self.distributions.append(random.randint(-100, 100))

    def generate_random_number(self, center, stddev):
        return random.gauss(center, stddev)

    def reward(self, action):
        return self.generate_random_number(self.distributions[action], self.STDDIVIATION)

    def info(self):
        print("[PROB DISTRIBUTIONS]")
        print(self.distributions)
        print("[END]")