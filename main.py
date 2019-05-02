#!/usr/bin/env python3
# Developer: Tim Roberts
# Description:
# If you live under a rock and are unfamiliar with this game:
# https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors

import random
# Needed for basic computer opponent


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):

        self.score = 0
        self.previousmove = None

    def move(self):
        # return 'rock'
        return moves[0]

    def learn(self, move):
        # Remember the opponents previous move:
        self.previousmove = move
        pass


# Player Types:
class HumanPlayer(Player):

    def move(self):

        choice = input('Make a choice:\nrock, paper, or scissors? ').lower()

        while choice != 'rock' and choice != 'paper' and choice != 'scissors':
            print('Sorry type "rock" "paper" or "scissors" ')
            choice = input('Make a choice:\nrock, ' +
                           'paper, or scissors? ').lower()
        return (choice)


class RandomPlayer(Player):
    # Select a random move choice each round
    def move(self):
        return (random.choice(moves))


class ReflectPlayer(Player):
    # Pick the opponents last move
    # First round default to rock
    def __init__(self):
        Player.__init__(self)
        self.previousmove = None

    def move(self):
        if self.previousmove is None:
            # First Round no previous move
            return (moves[0])
        else:
            # reflect previous choice
            return (self.previousmove)


class CyclePlayer(Player):
    # Cycle through choices Paper Rock then Scissors
    # Starts with Paper (Round 0)
    # Using the % (modulo) operator to track after the first 3 rounds

    def __init__(self):

        Player.__init__(self)
        # Track which round we are on:
        self.step = 0

    def move(self):
        choice = None
        if self.step < 3:
            if self.step == 0:
                # rock
                choice = moves[0]
                self.step += 1
            elif self.step == 1:
                # paper
                choice = moves[1]
                self.step += 1
            else:
                # scissors
                choice = moves[2]
                self.step += 1
        else:
            # More than 3 rounds this game
            choice = moves[self.step % 3]
            self.step += 1

        return choice


def beats(one, two):
    # Needs rework. Only tracks a win not ties
    # currently has to be called twice and if neither
    # are valid then that means it has to be a tie.
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2, rounds):
        self.p1 = p1
        self.p2 = p2

        # Keep track of wins (score1) / loses (score2) / ties (score3)
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.score1 += 1
            print("Player 1 Won this round!")
        elif beats(move2, move1):
            self.score2 += 1
            print("Player 2 Won this round!")
        else:
            self.score3 += 1
            print("It's a Draw this round!")

        print(f"Wins: {self.score1} Loses: {self.score2} " +
              "Ties: ", self.score3)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play_game(self):
        print("Game start!")
        for round in range(rounds):
            print(f"Round {round} of {rounds}:")
            self.play_round()

        # Final Score:
        if self.score1 > self.score2:
            print("Player 1 Wins the Game!")
            print(f"Wins: {self.score1} Loses: {self.score2} " +
                  "Ties: ", self.score3)
        elif self.score1 < self.score2:
            print("Player 2 Wins the Game!")
            print(f"Wins: {self.score2} Loses: {self.score2} " +
                  "Ties: ", self.score3)
        else:
            print("No Winner You Tied!")
            print(f"Wins: {self.score1} Loses: {self.score2} " +
                  "Ties: ", self.score3)
        print("Game over!")


if __name__ == '__main__':
    # Set how many rounds to play:
    rounds = 0
    while True:
        try:
            rounds = int(input('Enter the number of rounds you ' +
                               'want to play:  '))
        except ValueError:
            print("Enter the number of rounds (as a number ie: 4) " +
                  "you want to play: ")
            continue
        else:
            # End Loop
            break

    # Select Players:
    player_dict = {
      "computer": "RandomPlayer",
      "human": "HumanPlayer",
      "cycle": "CyclePlayer",
      "reflect": "ReflectPlayer"
    }

    player_text = """
Select which play style from one of the following:
'human' for the player to be a human
'computer' for the computer to play randomly
'reflect' for the computer to pick the opponents last move
'cycle' for the computer to cyle through choices predicatably:
    paper then rock then scissors repeating
    """
    print(player_text)
    player1 = None
    player2 = None

    while player1 not in player_dict or player2 not in player_dict:
        player1 = input("Enter Player 1: ").lower()
        player2 = input("Enter Player 2: ").lower()

    if player1 == 'human':
        p1 = HumanPlayer()
    elif player1 == 'computer':
        p1 = RandomPlayer()
    elif player1 == 'cycle':
        p1 = CyclePlayer()
    elif player1 == 'reflect':
        p1 = ReflectPlayer()

    if player2 == 'human':
        p2 = HumanPlayer()
    elif player2 == 'computer':
        p2 = RandomPlayer()
    elif player2 == 'cycle':
        p2 = CyclePlayer()
    elif player2 == 'reflect':
        p2 = ReflectPlayer()

    game = Game(p1, p2, rounds)
    game.play_game()
