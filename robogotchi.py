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

    def __init__(self, name):
        self.name = name
        self.total_count = {
            'won': 0,
            'robot_won': 0,
            'draws': 0
        }
        self.dict_info = {
            'battery': 100,
            'overheat': 0,
            'skills': 0,
            'boredom': 0,
            'rust': 0
        }
        self.rust_events = {
            0: None,
            10: f'Oh no, {self.name} stepped into a puddle!',
            30: f'Oh, {self.name} encountered a sprinkler!',
            50: f'Guess what! {self.name} fell into the pool!',
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
        print(f'\nYou won: {self.total_count["won"]},')
        print(f'The robot won: {self.total_count["robot_won"]},')
        print(f'Draws: {self.total_count["draws"]}.\n')

    def check_info(self):
        print(f'{self.name}\'s level of boredom was 0. Now it is {self.dict_info["boredom"]}')
        print(f'{self.name}\'s level of overheat was 0. Now it is {self.dict_info["overheat"]}.')

        if self.dict_info['boredom'] == 0:
            print(f'{self.name} is in a great mood!')

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

    def play(self):
        print('\nWhich game would you like to play?')
        while True:
            user_input = input()

            if user_input in ('Numbers', 'numbers'):
                self.process_task()
                exit()
            elif user_input in ('Rock-paper-scissors', 'rock-paper-scissors'):
                self.rock_paper_scissors()
                exit()
            else:
                print('\nPlease choose a valid option: Numbers or Rock-paper-scissors?')
                continue

        previous_rust = self.dict_info['rust']

        self.dict_info.update({
            'boredom': 0 if self.dict_info['boredom'] < 20 else self.dict_info['boredom'] - 20
        })

        rust = self.un_event_randint()

        if rust:
            print(f'\n{self.rust_events[rust]}')
            self.dict_info.update({'rust': self.dict_info['rust'] + rust})

        if self.get_prints_info() is not None:
            print(self.get_prints_info())

        if rust:
            print(f'{self.name}\'s level of rust was {previous_rust}. Now it is {self.dict_info["rust"]}.')

        if self.check_info() is not None:
            print(self.check_info())

    def info(self):
        print(f'{self.name}\'s stats are:')
        print(f'battery is {self.dict_info["battery"]},')
        print(f'overheat is {self.dict_info["overheat"]},')
        print(f'skill level is {self.dict_info["skills"]},')
        print(f'boredom is {self.dict_info["boredom"]},')
        print(f'rust is {self.dict_info["rust"]}.')

    def sleep(self):
        if self.dict_info['overheat'] > 0:
            previous_overheat = self.dict_info['overheat']

            if self.dict_info['overheat'] < 20:
                self.dict_info.update({'overheat': 0})
            else:
                self.dict_info.update({'overheat': self.dict_info['overheat'] - 20})

            if self.dict_info['overheat'] == 0:
                print(f'\n{self.name} is cool!')
            else:
                print(f'\n{self.name} cooled off!')

            print(f'{self.name}\'s level of overheat was {previous_overheat}. '
                  f'Now it is {self.dict_info["overheat"]}.')
        else:
            print(f'\n{self.name} is cool!')
            print(f'{self.name}\'s level of overheat was 0. Now it is {self.dict_info["overheat"]}.')

    def recharge(self):
        if self.dict_info['battery'] == 100:
            print(f'{self.name} is charged!')
        else:
            previous_battery = self.dict_info['battery']
            previous_boredom = self.dict_info['boredom']
            previous_overheat = self.dict_info['overheat']

            self.dict_info.update({
                'battery': self.dict_info['battery'] + 10,
                'boredom': self.dict_info['boredom'] + 5
            })

            if self.dict_info['overheat'] != 0:
                self.dict_info.update({
                    'overheat': self.dict_info['overheat'] - 5
                })

            print(f'\n{self.name}\'s level of overheat was {previous_overheat}. Now it is {self.dict_info["overheat"]}.')
            print(f'{self.name}\'s level of the battery was {previous_battery}. Now it is {self.dict_info["battery"]}.')
            print(f'{self.name}\'s level of boredom was {previous_boredom}. Now it is {self.dict_info["boredom"]}.')
            print(f'\n{self.name} is recharged!')

    def learn(self):
        if self.dict_info['skills'] == 100:
            print(f'There\'s nothing for {self.name} to learn!')
        else:
            skill_previous = self.dict_info['skills']
            overheat_previous = self.dict_info['overheat']
            battery_previous = self.dict_info['battery']
            boredom_previous = self.dict_info['boredom']
            rust_previous = self.dict_info['rust']

            self.dict_info.update({
                'battery': 0 if self.dict_info['battery'] < 10 else self.dict_info['battery'] - 10,
                'overheat': self.dict_info['overheat'] + 10,
                'skills': self.dict_info['skills'] + 10,
                'boredom': self.dict_info['boredom'] + 5
            })

            rust = self.un_event_randint()

            if rust:
                print(f'\n{self.rust_events[rust]}')

            print(f'\n{self.name}\'s level of skill was {skill_previous}. Now it is {self.dict_info["skills"]}.')
            print(f'{self.name}\'s level of overheat was {overheat_previous}. Now it is {self.dict_info["overheat"]}.')
            print(f'{self.name}\'s level of the battery was {battery_previous}. Now it is {self.dict_info["battery"]}.')
            print(f'{self.name}\'s level of boredom was {boredom_previous}. Now it is {self.dict_info["boredom"]}.')
            if rust:
                self.dict_info.update({'rust': self.dict_info['rust'] + rust})
                print(f'{self.name}\'s level of rust was {rust_previous}. Now it is {self.dict_info["rust"]}.')
            print(f'\n{self.name} has become smarter!\n')

    def oil(self):
        if self.dict_info['rust'] == 0:
            print(f'{self.name} is fine, no need to oil!')
        else:
            previous_rust = self.dict_info['rust']

            if self.dict_info['rust'] < 20:
                self.dict_info.update({'rust': 0})
            else:
                self.dict_info.update({'rust': self.dict_info['rust'] - 20})

            print(f'{self.name}\'s level of rust was {previous_rust}. Now it is {self.dict_info["rust"]}. {self.name} '
                  f'is less rusty!')

    def work(self):
        if self.dict_info['skills'] < 50:
            print(f'{self.name} has got to learn before working!')
        else:
            rust_previous = self.dict_info['rust']
            overheat_previous = self.dict_info['overheat']
            battery_previous = self.dict_info['battery']
            boredom_previous = self.dict_info['boredom']

            self.dict_info.update({
                'battery': 0 if self.dict_info['battery'] < 10 else self.dict_info['battery'] - 10,
                'overheat': self.dict_info['overheat'] + 10,
                'boredom': self.dict_info['boredom'] + 10
            })

            rust = self.un_event_randint()

            if rust:
                print(f'\n{self.rust_events[rust]}')

            print(f'\n{self.name}\'s level of boredom was {boredom_previous}. Now it is {self.dict_info["boredom"]}.')
            print(f'{self.name}\'s level of overheat was {overheat_previous}. Now it is {self.dict_info["overheat"]}.')
            print(f'{self.name}\'s level of the battery was {battery_previous}. Now it is {self.dict_info["battery"]}.')
            if rust:
                self.dict_info.update({'rust': self.dict_info['rust'] + rust})
                print(f'{self.name}\'s level of rust was {rust_previous}. Now it is {self.dict_info["rust"]}.')

            print(f'\n{self.name} did well!\n')

    def un_event_randint(self):
        rust = choice(list(self.rust_events))
        return rust

    def menu(self):
        options = ['exit', 'info', 'recharge', 'sleep', 'play', 'oil', 'work', 'learn']

        while True:
            print(f'\nAvailable interactions with {self.name}:')
            print('exit – Exit')
            print('info – Check the vitals')
            print('work – Work')
            print('play – Play')
            print('oil – Oil')
            print('recharge – Recharge')
            print('sleep – Sleep mode')
            print('learn – Learn skills')

            choice_menu = input('\nChoose:\n')

            if choice_menu in options:
                return choice_menu
            else:
                print('\nInvalid input, try again!')
                continue

    @staticmethod
    def exit(message='Game over.'):
        print(message)
        exit()

    def run(self):
        while True:

            if self.dict_info['overheat'] > 100:
                message = f'The level of overheat reached 100, {self.name} has blown up! Game over. Try again?'
                self.exit(message)

            elif self.dict_info['rust'] > 100:
                message = f'{self.name} is too rusty! Game over. Try again?'
                self.exit(message)

            check_input = self.menu()

            if self.dict_info['battery'] == 0 and check_input != 'recharge':
                print(f'The level of the battery is 0, {self.name} needs recharging!\n')
                continue
            elif self.dict_info['boredom'] == 100 and check_input != 'play':
                print(f'{self.name} is too bored! {self.name} needs to have fun!.\n')
                continue

            if check_input == 'info':
                self.info()
            elif check_input == 'sleep':
                self.sleep()
            elif check_input == 'play':
                self.play()
            elif check_input == 'recharge':
                self.recharge()
            elif check_input == 'learn':
                self.learn()
            elif check_input == 'work':
                self.work()
            elif check_input == 'oil':
                self.oil()
            elif check_input == 'exit':
                self.exit()


def main():
    name_input = input('How will you call your robot?\n')

    robo_number = RoboGoNumber(name_input)
    robo_number.run()


if __name__ == '__main__':
    main()