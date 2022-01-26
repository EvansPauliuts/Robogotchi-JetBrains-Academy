# Robogotchi-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/135

## Work on project. Stage 2/4: Rock-Paper-Scissors
### Objectives

In this stage, your program should:

1. Prompt the user to pick a game with a message ```Which game would you like to play?```.
2. If they choose "Numbers", proceed with the game as in the previous stage. If they choose rock-paper-scissors, 
implement steps 3-6. If the user input is anything else than "Numbers" or "Rock-paper-scissors", 
print ```Please choose a valid option: Numbers or Rock-paper-scissors?```.
3. Take the user input, check its validity, and ask for a valid input if needed.
4. Output the robot's move: ```The robot chose [paper/rock/scissors]```.
5. Output the result using an appropriate message: ```You won!```, ```The robot won!```, or ```It's a draw!```.
6. Keep taking input as long as the user wants to play.
7. Keep the game statistics and print it when the user decides to exit the game.

#### Examples
The greater-than symbol followed by a space (>) represents the user input.

##### example 1
```shell
Which game would you like to play?
> Rock-paper-scissors

What is your move?
> Paper
The robot chose paper
It's a draw!

What is your move?
> rock
The robot chose scissors
You won!

What is your move?
> gun
No such option! Try again!

What is your move?
> scissors
The robot chose paper
You won!

What is your move?
> exit game

You won: 2,
The robot won: 0,
Draws: 1
```

##### example 2
```shell
Which game would you like to play?
> Dominoes

Please choose a valid option: Numbers or Rock-paper-scissors?

> Numbers

What is your number?
> exit game

You won: 0,
The robot won: 0,
Draws: 0.
```
