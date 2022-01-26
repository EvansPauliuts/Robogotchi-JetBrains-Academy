# Robogotchi-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/135

## Work on project. Stage 1/4: The game of numbers
### Objectives

In this stage, your program should:

1. Take the user's input, check its validity, and ask again for a valid input if needed.
2. If the user provides an invalid option, the program has to display an appropriate message.
All three invalid options — negative numbers, text strings, and numbers over 1,000,000 — have to be handled differently.
3. Output the result of the game.
4. Keep taking the input as long as the user wants to play.
5. Collect the game statistics and print it when the user decides to exit the game.

#### Examples
The greater-than symbol followed by a space (>) represents the user input.

##### example 1
```shell
What is your number?
> -54

The number can't be negative!

What is your number?
> 45

The robot entered the number 810376.
The goal number is 63419.
You won!

What is your number?
> exit game

You won: 1,
The robot won: 0,
Draws: 0.
```

##### example 2
```shell
What is your number?
> 5000001

Invalid input! The number can't be bigger than 1000000.

What is your number?
> 654

The robot entered the number 235945.
The goal number is 875951.
The robot won!

What is your number?
> 123123

The robot entered the number 810808.
The goal number is 875951.
The robot won!

What is your number?
> 432443

The robot entered the number 555335.
The goal number is 875951.
The robot won!

What is your number?
> pineapple

A string is not a valid input!

What is your number?
> exit game

You won: 0,
The robot won: 3,
Draws: 0.
```
