import random
moves = ['rock', 'paper', 'scissors']


class Player:
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class ReflectPlayer(Player):
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'scissors':
            return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):

        while True:
            move = input("choose rock, paper, scissors >> ").lower()
            if move in moves:
                return move
            print('Invalid...')


def beats(one, two):
    return ((one == 'paper' and two == 'rock') or
            (one == 'scissors' and two == 'paper') or
            (one == 'rock' and two == 'scissors'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.count = 0
        self.p2.count = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1.count += 1
        elif move1 == move2:
            print("You two are like each other")
        else:
            self.p2.count += 1
        print(
            f"player one have : {self.p1.count} and\
                    player two have : {self.p2.count}")
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)

    def play_game(self):
        print("Game start!")
        rounds = int(input("How many round do you want to play? "))
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.count > self.p2.count:
            print(
                f'the Player one is win and the scorse are ::\
                    Player one is {self.p1.count} an player two is\
                        {self.p2.count}')
        elif self.p1.count < self.p2.count:
            print(
                f'the Player two is win and the scorse are ::\
                    Player one is {self.p1.count} an player two is\
                        {self.p2.count}')
        else:
            print(
                f'The score is equal and the scorse are ::\
                    Player one is {self.p1.count} an player two is\
                        {self.p2.count}')
        print("Game over!")


if __name__ == '__main__':
    players = [AllRockPlayer(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
