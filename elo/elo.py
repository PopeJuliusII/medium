import numpy as np
import matplotlib.pyplot as plt


class Player():
    def __init__(self, elo):
        self.elo = elo
        self.k = 32

    def defeated(self, opponent):
        self.update_elo(1, opponent)

    def draw_with(self, opponent):
        self.update_elo(0.5, opponent)

    def lose_to(self, opponent):
        self.update_elo(0, opponent)

    def update_elo(self, outcome, opponent):
        expected_self = self.calculate_expected(opponent)
        expected_opponent = opponent.calculate_expected(self)
        self.elo += round(self.k * (outcome - expected_self))
        opponent.elo += round(opponent.k * ((1 - outcome) - expected_opponent))

    def calculate_expected(self, opponent):
        return (1 + 10 ** ((opponent.elo - self.elo)/400)) ** -1


if __name__ == "__main__":
    jack, jill = Player(1200), Player(1200)
    jack_elo, jill_elo = [], []

    for result in [1, 1, 1, 0] * 30:
        jack_elo.append(jack.elo)
        jill_elo.append(jill.elo)
        if result == 1:
            jack.defeated(jill)
        elif result == 0:
            jack.lose_to(jill)
        else:
            jack.draw_with(jill)

    plt.plot(np.array([jack_elo, jill_elo]).T)
    plt.show()
