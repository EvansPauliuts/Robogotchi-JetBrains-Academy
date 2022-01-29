# Robogotchi-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/135

## Work on project. Stage 3/4: A simple robot
### Objectives

In this stage, your program should:

1. Provide the following interactions: playing, recharging, sleeping;
2. Print the information about the robot: its level of battery, boredom, overheating, and skill;
3. Provide an option to quit the game;
4. Take the user's input;
5. If the input is correct, the chosen interaction should be performed. Otherwise, the program should inform the user and ask them for a valid input;
6. React when certain parameters reach critical levels.

#### Examples
The greater-than symbol followed by a space (>) represents the user input.

##### example 1
```shell
How will you call your robot?
> Daniel

Available interactions with Daniel:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play

Choose:
> info

Daniel's stats are: the battery is 100,
overheat is 0,
skill level is 0,
boredom is 0.

Available interactions with Daniel:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play

Choose:
> fly to the moon

Invalid input, try again!

Available interactions with Daniel:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play

Choose:
> sleep

Daniel is cool!

Available interactions with Daniel:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play

Choose:
> play

Which game would you like to play?
> Rock-paper-scissors

What is your move?
> rock

The robot chose scissors
You won!

What is your move?
> paper

The robot chose scissors
The robot won!

What is your move?
> rock

The robot chose paper
The robot won!

What is your move?
> exit game

You won: 1,
The robot won: 2,
Draws: 0.

Daniel's level of boredom was 0. Now it is 0.
Daniel's level of overheat was 0. Now it is 10.
Daniel is in a great mood!

Available interactions with Daniel:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play

Choose:
> recharge

Daniel is charged!

Available interactions with Daniel:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play

Choose:
> sleep

Daniel's level of overheat was 10. Now it is 0.

Daniel is cool!

Available interactions with Daniel:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play

Choose:
> exit

Game over
```

##### example 2
```shell
Choose:
> play

Which game would you like to play?
> numbers

What is your number?
> 678

The robot entered the number 518807.
The goal number is 873547
The robot won!

What is your number?
> 6

The robot entered the number 91265.
The goal number is 374818
The robot won!

What is your number?
> exit game

You won: 0,
The robot won: 2,
Draws: 0.

Daniel's level of boredom was 0. Now it is 0.
Daniel's level of overheat was 80. Now it is 90.
Daniel is in a great mood!

Available interactions with Daniel:
exit - Exit
info - Check the vitals
recharge - Recharge
sleep - Sleep mode
play - Play

Choose:
> play

Which game would you like to play?
> Rock-paper-scissors

What is your move?
> paper

The robot chose rock
You won!

What is your move?
> exit game

The level of overheat reached 100, Daniel has blown up! Game over. Try again?
```
