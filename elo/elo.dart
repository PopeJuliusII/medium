import 'dart:math';

class Player {
  static const int k = 32;
  int elo;

  Player({this.elo = 1200});

  void updateElo({Player opponent, double outcome}) {
    double expectedPersonOne = this.calculateExpected(opponent: opponent);
    double expectedPersonTwo = opponent.calculateExpected(opponent: this);
    this.elo += num.parse(
        (Player.k * (outcome - expectedPersonOne)).toStringAsFixed(0));
    opponent.elo += num.parse(
        (Player.k * ((1 - outcome) - expectedPersonTwo)).toStringAsFixed(0));
  }

  double calculateExpected({Player opponent}) {
    // Expected for personOne vs personTwo
    return num.parse(pow((1 + pow(10, ((opponent.elo - this.elo) / 400))), -1)
        .toStringAsFixed(5));
  }
}
