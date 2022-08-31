# Minesweeper
During winter break of my freshman year I decided to recreate the game Minesweeper in python as a way to self teach myself the programming language.

When I started the project I had no knowledge of how to program in Python at all. Armed with just knowledge of java and object-oriented programming, I challenged myself to recreate the classic Minesweeper.

Later on I revisited this project whilst interested in AI. I created a solving AI that could solve the game.

![Alt Text](https://i.imgur.com/ljSjXRP.gif)


To run the programs you must first have pygame installed. 
To install pygame run "python -m pip install pygame" in the commandline.

"python Minesweeper.py" to run the game. You'll have to input height, width, and number of mines in the commandline

"python Solver.py" to run the simple AI that will try to finish the game. You'll have to input height, width, and number of mines in the commandline and also 
clear the first tile.

Notes: I haven't coded all the checks to make sure you're not trying to break the game. This was a little project and I'm happy with where I've taken it. 
       The Solver might get stuck. It's able to clear simple checks. It's not able to clear tiles that require more advanced methods. 
