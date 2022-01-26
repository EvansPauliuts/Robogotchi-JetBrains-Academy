# Write your code here
from random import randint


class NegativeError(Exception):
    def __str__(self):
        return '\nThe number can\'t be negative!\n'


class RangeError(Exception):
    def __str__(self):
        return '\nInvalid input! The number can\'t be bigger than 1000000.\n'


class RoboGoNumber:
    MIN_NUM = 1
    MAX_NUM = 1_000_000

    def __init__(self):
        self.total_count = {
            'won': 0,
            'robot_won': 0,
            'draws': 0
        }

    def process_task(self, input_str):
        try:
            input_num = int(input_str)

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

    def run(self):
        while True:
            user_input = input('What is your number?\n')

            if user_input == 'exit game':
                self.get_prints_info()
                break
            else:
                self.process_task(user_input)

    def get_prints_info(self):
        print(f'\nYou won: {self.total_count["won"]},\n'
              f'The robot won: {self.total_count["robot_won"]},\nDraws: {self.total_count["draws"]}.')


def main():
    robo_number = RoboGoNumber()
    robo_number.run()


if __name__ == '__main__':
    main()
