# Mat[c]hed
## This project is a Two-player competitive game in matching 15 pairs of cards and there is a single-player mode that races against time with a scoreboard system.

Rules:
1. Starts with 30 cards faced-down 

2. Player starts opening 2 pairs of cards if they match 
score +=??? (according to card difficulty and time bonus) to the player and continue to open another pair and repeat until the cards don’t match.

3. Another player starts to open the cards and repeats steps 2-3

4. The first player who reaches a score of 8 wins the game.

note: There are timers of 10 seconds counting down between each player's turn if the timer runs out the turn skips.

## Required libraries
* json - used to save player's score
* time - used to create a class Timer
* random - used to random new card's positions everygame

## Program design
* Player : used to store player data (name, score, time)
* Card : used to create a card with position, faced down/up, difficulty
* Scoreboard : used to open the json file
* Timer : used to make the timer for the game
* Game : used to construct all of the classes above and run the game

## Code structure
* main.py : contains Card Game and Scoreboard
* Game.py : contains Game class
* Card.py : contains Card class
* Player.py : contains Player class
* Scoreboard.py : contains Scoreboard class
* Timer.py : contains Timer class
* scoreboard.json : used to save player name and score
* card_data.json : used to save equations 

