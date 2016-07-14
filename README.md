# Insaniquarium
This is my attempt at making the game [Insaniquarium](http://www.popcap.com/insaniquarium)

# Requirements
- After cloning the repository go to the its directory and execute these commands:
```
$ python3 setup.py build
$ python3 setup.py install
```
Note: It should install insaniquarium in `/usr/local/lib/python3.4/dist-packages` by default. (At least it did on my computer, requires administrator's permission to install there though.)

- You must have PyQt5 on your computer in order to run the game. If you don't, install the `python3-pyqt5` package using your system's package manager, for example:
```
$ sudo apt-get install python3-pyqt5
```

- To run the game itself, simply execute:
```
$ insaniquarium
```
Alternatively, you can go to `/Insaniquarium/insaniquarium/gui` and compile the `ui.py` file to run the game:
```
$ python3 ui.py
```

# Gameplay

The game immerses us in the world of fishes. The player is given an aquarium with fish. He must take care of them and protect them from hungry aliens.

-   Fish

The fish grow up if you feed them, but they can also get sick and die if they are not fed frequently. When a fish grows it starts dropping money. To feed a fish simply click on an empty portion of the aquarium and food will drop. Be mindful of the fact that food costs money!

-   Aliens

The aquarium is not a safe haven where you just take care of fishes. Aliens that try to eat your fish will spawn from time to time. These aliens can be killed by you with a weapon. To kill a monster simply click on it repeatedly. Did I mention that aliens vary in strength? Shoot as fast as you can!

-   Money

You can use money to buy more fish and upgrade the quality of the food and the power of your weapon. To collect money simply click on a sinking coin, but be swift, because it's lost forever if it touches the seabed. Money also act as your total score in the game.


# Additional functionality

-   Graphical environment, implemented with PyQt5.
-   Main menu - contains all the game options.
-   Pause - You can enter the main menu and the game will be paused automatically.
-   Sidebar where you score is shown that also provides buttons for buying fish and upgrading food quality and weapon power. Also has menu button.
