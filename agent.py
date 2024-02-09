from setting import Bandits
from numpy import random as nrandom
import random

class Agent:
    def __init__(self, epsilon=0.01, k=10, initial=0):
        self.epsilon = epsilon
        self.k = k

        self.counts = [0] * self.k
        self.qtable = [initial] * self.k

    def make_action(self):
        decision = nrandom.choice([0, 1], p=[self.epsilon, 1 - self.epsilon])
        if decision == 0:
            return random.randint(0, self.k - 1)

        maxi = -1000
        best_action = -1
        for action in range(self.k):
            if self.qtable[action] > maxi:
                maxi = self.qtable[action]
                best_action = action

        return best_action

    def set_new_reward(self, action, reward):
        self.counts[action] += 1
        self.qtable[action] = self.qtable[action] + (1 / self.counts[action]) * (reward - self.qtable[action])

    def info(self):
        print("[AGENT INFO]")
        print(self.qtable)
        print("[END]")

