# Write your code here
from random import randint, choice
from enum import Enum


class NegativeError(Exception):
    def __str__(self):
        return '\nThe number can\'t be negative!\n'


class RangeError(Exception):
    def __str__(self):
        return '\nInvalid input! The number can\'t be bigger than 1000000.\n'


class RandomRPS(Enum):
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'


class RoboGoNumber:
    MIN_NUM = 1
    MAX_NUM = 1_000_000

    def __init__(self):
        self.total_count = {
            'won': 0,
            'robot_won': 0,
            'draws': 0
        }

    def process_task(self):
        while True:
            user_val = input('\nWhat is your number?\n')

            if user_val == 'exit game':
                break
            else:
                try:
                    input_num = int(user_val)

                    if input_num < RoboGoNumber.MIN_NUM:
                        raise NegativeError
                    elif input_num > RoboGoNumber.MAX_NUM:
                        raise RangeError

                except ValueError:
                    print('\nA string is not a valid input\n')
                except NegativeError as e:
                    print(e)
                except RangeError as e:
                    print(e)
                else:
                    self.process_compute(input_num)

    def process_compute(self, b):
        randint_number = randint(RoboGoNumber.MIN_NUM, RoboGoNumber.MAX_NUM)
        robot_randint_number = randint(RoboGoNumber.MIN_NUM, RoboGoNumber.MAX_NUM)

        print(f'\nThe robot entered the number {robot_randint_number}.')
        print(f'The goal number is {randint_number}.')

        user_val = abs(int(b) - randint_number)
        robot_val = abs(robot_randint_number - randint_number)

        if user_val < robot_val:
            self.total_count['won'] += 1
            print('You won!\n')
        elif user_val == robot_val:
            self.total_count['draws'] += 1
        else:
            self.total_count['robot_won'] += 1
            print('The robot won!')

    def get_prints_info(self):
        print(f'\nYou won: {self.total_count["won"]},\n'
              f'The robot won: {self.total_count["robot_won"]},\nDraws: {self.total_count["draws"]}.')
        print()

    @staticmethod
    def winner_check(a, b):
        winning_dict = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

        if a in winning_dict.keys():
            return a if b == winning_dict[a] else b

    def rock_paper_scissors(self):
        while True:
            user_val = input('\nWhat is your move?\n')
            robot_random = choice(list(RandomRPS))

            if user_val == robot_random.value:
                self.total_count['draws'] += 1
                print(f'The robot chose {robot_random.value}')
                print(f'It\'s a draw!')
            elif user_val == self.winner_check(user_val, robot_random.value):
                self.total_count['won'] += 1
                print(f'The robot chose {robot_random.value}')
                print('You won!')
            elif user_val == 'exit game':
                break
            elif user_val not in ['paper', 'scissors', 'rock']:
                print('No such option! Try again!')
            else:
                self.total_count['robot_won'] += 1
                print(f'The robot chose {robot_random.value}')
                print('The robot won!')

    def run(self):
        print('Which game would you like to play?')
        while True:
            user_input = input()

            if user_input in ('Numbers', 'numbers'):
                self.process_task()
                break
            elif user_input in ('Rock-paper-scissors', 'rock-paper-scissors'):
                self.rock_paper_scissors()
                break
            else:
                print('\nPlease choose a valid option: Numbers or Rock-paper-scissors?')
                continue

        if self.get_prints_info() is not None:
            print(self.get_prints_info())


def main():
    robo_number = RoboGoNumber()
    robo_number.run()


if __name__ == '__main__':
    main()
