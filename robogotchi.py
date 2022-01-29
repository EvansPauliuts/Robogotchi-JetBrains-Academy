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
        self.dict_info = {
            'battery': 100,
            'overheat': 0,
            'skills': 0,
            'boredom': 0
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

        self.play_dict_result()

    def play_dict_result(self):
        boredom_zero = self.dict_info['boredom'] - 20

        self.dict_info.update({
            'boredom': 0 if boredom_zero < 0 else boredom_zero,
            'overheat': self.dict_info['overheat'] + 10
        })

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

    def check_info(self, name):
        print(f'{name}\'s level of boredom was 0. Now it is {self.dict_info["boredom"]}.\n{name}\'s level of overheat '
              f'was 0. Now it is {self.dict_info["overheat"]}.')
        if self.dict_info['boredom'] == 0:
            print(f'{name} is in a great mood!')

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

        self.play_dict_result()

    def run(self):
        name_input = input('How will you call your robot?\n')

        while True:
            print(f'\nAvailable interactions with {name_input}:\nexit - Exit\ninfo - Check the vitals\n'
                  'recharge - Recharge\nsleep - Sleep mode\nplay - Play')

            check_input = input('\nChoose:\n')

            if self.dict_info['overheat'] <= 100:
                print(f'\nThe level of overheat reached 100, {name_input} has blown up! Game over. Try again?')
                break

            if check_input == 'info':
                print(f'{name_input.title()}\'s stats are: the battery is 100,\noverheat is '
                      f'{self.dict_info["overheat"]},\nskill level is {self.dict_info["skills"]},\nboredom '
                      f'is {self.dict_info["boredom"]}.')
                continue
            elif check_input == 'sleep':
                if self.dict_info['overheat'] > 0:
                    previous_overheat = self.dict_info['overheat']
                    res_over = self.dict_info['overheat'] - 20
                    self.dict_info.update({'overheat': self.dict_info['overheat'] - 20})

                    if res_over < 0:
                        self.dict_info.update({'overheat': 0})

                    if self.dict_info['overheat'] == 0:
                        print(f'\n{name_input} is cool!')
                    else:
                        print(f'\n{name_input} cooled off!')

                    print(f'{name_input}\'s level of overheat was {previous_overheat}. '
                          f'Now it is {self.dict_info["overheat"]}.')
                else:
                    print(f'\n{name_input} is cool!')
                    print(f'{name_input}\'s level of overheat was 0. '
                          f'Now it is {self.dict_info["overheat"]}.')

                continue
            elif check_input == 'play':
                print('\nWhich game would you like to play?')
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
                if self.check_info(name=name_input.title()) is not None:
                    print(self.check_info(name=name_input.title()))

                self.total_count.update({'won': 0, 'robot_won': 0, 'draws': 0})

            elif check_input == 'recharge':
                if self.dict_info['battery'] == 100:
                    print(f'{name_input} is charged!')
                else:
                    previous_battery = self.dict_info['battery']
                    boredom_battery = self.dict_info['boredom']
                    overheat_battery = self.dict_info['overheat']

                    self.dict_info.update({
                        'battery': self.dict_info['battery'] + 10,
                        'overheat': self.dict_info['overheat'] - 5,
                        'boredom': self.dict_info['boredom'] + 5
                    })
                    print(f'{name_input.title()}\'s level of overheat was {overheat_battery}. Now it '
                          f'is {self.dict_info["overheat"]}.\n{name_input.title()}\'s level of the battery was '
                          f'{previous_battery}. Now it is {self.dict_info["battery"]}.\n{name_input.title()}\'s '
                          f'level of boredom was {boredom_battery}. Now it is {self.dict_info["boredom"]}.\n'
                          f'{name_input.title()}\'s is recharged!')

            elif check_input == 'exit':
                print('Game over')
                break
            else:
                print('\nInvalid input, try again!')


def main():
    robo_number = RoboGoNumber()
    robo_number.run()


if __name__ == '__main__':
    main()
