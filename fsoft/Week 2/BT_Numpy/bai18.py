import random

def input_number(prompt='Please enter a number: ', minimum=0, maximum=None):

    while True:
        try:
            number = abs(int(input(prompt)))
            break

        except ValueError:
            print('Type again!')

    return number

class RolledOneException(Exception):
    pass


class Die:

    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):

        self.value = random.randint(1, 6)
        if self.value == 1:
            raise RolledOneException

        return self.value


    def __str__(self):
        return "Rolled " + str(self.value) + "."


class Box:
    def __init__(self):
        self.value = 0

    def reset(self):
        self.value = 0

    def add_dice_value(self, dice_value):
        self.value += dice_value

class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.score = 0

    def add_score(self, player_score):
        self.score += player_score

    def __str__(self):
        return str(self.name) + ": " + str(self.score)

class HumanPlayer(Player):
    def __init__(self, name):
        super(HumanPlayer, self).__init__(name)


    def keep_rolling(self, box):

        human_decision = input_number("1 - Continue, 0 - Hold: ", 0, 1)
        if human_decision == 1:
            return True
        else:
            return False


class GameManager:
    def __init__(self, humans=1):

        self.players = []
        if humans == 1:
            self.players.append(HumanPlayer('Human'))
        else:
            for i in range(humans):
                player_name = input('Name of  {}: '.format(i+1))
                self.players.append(HumanPlayer(player_name))

        self.no_of_players = len(self.players)

        self.die = Die()
        self.box = Box()


    def decide_first_player(self):
        self.current_player = random.randint(1, self.no_of_players) % self.no_of_players
        print('{} starts'.format(self.players[self.current_player].name))

    def next_player(self):
        self.current_player = (self.current_player + 1) % self.no_of_players

    def previous_player(self):
        self.current_player = (self.current_player - 1) % self.no_of_players

    def get_all_scores(self):
        return ', '.join(str(player) for player in self.players)


    def play_game(self):

        self.decide_first_player()

        while all(player.score < 100 for player in self.players):
            print('\n{}'.format(self.get_all_scores()))
            print('\nTurn of {}'.format(self.players[self.current_player].name))
            self.box.reset()

            while self.keep_rolling():
                pass

            self.players[self.current_player].add_score(self.box.value)
            self.next_player()

        self.previous_player()
        print(' {} has won '.format(self.players[self.current_player].name).center(70, '*'))


    def keep_rolling(self):

        try:
            dice_value = self.die.roll()
            self.box.add_dice_value(dice_value)
            print('Dice: {}, Score at this turn: {}'.format(dice_value, self.box.value))

            return self.players[self.current_player].keep_rolling(self.box)

        except RolledOneException:
            self.box.reset()
            return False

def main():

    human_players = input_number('Number of players: ')
    game_manager = GameManager(human_players)
    game_manager.play_game()

if __name__ == '__main__':
    main()