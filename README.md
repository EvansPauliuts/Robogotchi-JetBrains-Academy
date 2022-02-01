# Robogotchi-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/135

## Work on project. Stage 4/4: Robogotchi
### Objectives

1. Offer the following interactions: oiling, learning, recharging, sleeping, playing, and working;
2. Take the user's input and call a suitable method if the input is valid;
3. Otherwise, the program should inform the user and ask for a valid input;
4. In case of an unpleasant event, the program should react to it.

#### Examples
The greater-than symbol followed by a space (>) represents the user input.

##### example 1
```shell
How will you call your robot?
> Daneel

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> learn

Daneel's level of skill was 0. Now it is 10.
Daneel's level of overheat was 0. Now it is 10.
Daneel's level of the battery was 100. Now it is 90.
Daneel's level of boredom was 0. Now it is 5.

Daneel has become smarter!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> oil

Daneel is fine, no need to oil!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> learn

Daneel's level of skill was 10. Now it is 20.
Daneel's level of overheat was 10. Now it is 20.
Daneel's level of the battery was 90. Now it is 80.
Daneel's level of boredom was 5. Now it is 10.

Daneel has become smarter!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> work

Daneel has got to learn before working!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> play
Which game would you like to play?
> numbers
What is your number?
> 678

The robot entered the number 483806.
The goal number is 980924
The robot won!

What is your number?
> 6755

The robot entered the number 7676.
The goal number is 980924
The robot won!

What is your number?
> 99876

The robot entered the number 969910.
The goal number is 980924
The robot won!

What is your number?
> exit game

You won: 0,
The robot won: 3,
Draws: 0.

Daneel's level of overheat was 20. Now it is 30.
Daneel's level of boredom was 10. Now it is 0.

Daneel is in a great mood!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> learn

Daneel's level of skill was 20. Now it is 30.
Daneel's level of overheat was 30. Now it is 40.
Daneel's level of the battery was 80. Now it is 70.
Daneel's level of boredom was 0. Now it is 5.

Daneel has become smarter!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> sleep

Daneel's level of overheat was 40. Now it is 20.

Daneel cooled off!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> learn

Daneel's level of skill was 30. Now it is 40.
Daneel's level of overheat was 20. Now it is 30.
Daneel's level of the battery was 70. Now it is 60.
Daneel's level of boredom was 5. Now it is 10.

Daneel has become smarter!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> exit

Game over
```

##### example 2
```shell
Choose:
> work

Oh no, Daneel stepped into a puddle!

Daneel's level of boredom was 40. Now it is 50.
Daneel's level of overheat was 35. Now it is 45.
Daneel's level of the battery was 30. Now it is 20.
Daneel's level of rust was 0. Now it is 10.

Daneel did well!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> sleep

Daneel's level of overheat was 45. Now it is 25.

Daneel cooled off!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> work

Guess what! Daneel fell into the pool!

Daneel's level of boredom was 50. Now it is 60.
Daneel's level of overheat was 25. Now it is 35.
Daneel's level of the battery was 20. Now it is 10.
Daneel's level of rust was 10. Now it is 60.

Daneel did well!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills


Choose:
> work

Guess what! Daneel fell into the pool!
Daneel is too rusty! Game over. Try again?
```

##### example 3
```shell
Choose:
> learn

Oh no, Daneel stepped into a puddle!

Daneel's level of skill was 80. Now it is 90.
Daneel's level of overheat was 60. Now it is 70.
Daneel's level of the battery was 20. Now it is 10.
Daneel's level of boredom was 40. Now it is 45.
Daneel's level of rust was 10. Now it is 20.

Daneel has become smarter!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> learn

Guess what! Daneel fell into the pool!

Daneel's level of skill was 90. Now it is 100.
Daneel's level of overheat was 70. Now it is 80.
Daneel's level of the battery was 10. Now it is 0.
Daneel's level of boredom was 45. Now it is 50.
Daneel's level of rust was 20. Now it is 70.

Daneel has become smarter!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> learn

The level of the battery is 0, Daneel needs recharging!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> learn

The level of the battery is 0, Daneel needs recharging!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> recharge

Daneel's level of overheat was 80. Now it is 75.
Daneel's level of the battery was 0. Now it is 10.
Daneel's level of boredom was 50. Now it is 55.


Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> exit

Game over
```

##### example 4
```shell
Choose:
> recharge

Daneel's level of overheat was 25. Now it is 20.
Daneel's level of the battery was 80. Now it is 90.
Daneel's level of boredom was 90. Now it is 95.

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> info

Daneel's stats are:
the battery is 90,
overheat is 20,
skill level is 100,
boredom is 95,
rust is 0.

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> recharge

Daneel's level of overheat was 20. Now it is 15.
Daneel's level of the battery was 90. Now it is 100.
Daneel's level of boredom was 95. Now it is 100.

Daneel is recharged!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> sleep

Daneel is too bored! Daneel needs to have fun!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> recharge

Daneel is too bored! Daneel needs to have fun!

Available interactions with Daneel:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:
> play

Which game would you like to play?
```