| Function Name          | Domain (inputs) | Range (outputs) | Behavior                                                     |
| ---------------------- | --------------- | --------------- | :----------------------------------------------------------- |
| create_map()           | N/A             | N/A             | Create one "screen" of object: 640 x 640                     |
| animate(scroll)        | boolean         | N/A             | Redraw the screen, including all sprites                     |
| show_game_over(result) | text            | N/A             | Show game over text on screen (show different text depending on the result.) |

### IronManClass

| Thread Name                | Domain (inputs) | Range (outputs) | Behavior                                                     |
| :------------------------- | --------------- | --------------- | :----------------------------------------------------------- |
| \__init__(self)            | object          | N/A             | Initiate instance variables                                  |
| show_stamina(self, damage) | object, boolean | N/A             | Displays the strength of Iron Man on the screen.             |
| turn(self, direction)      | object, integer | list(speed)     | Returns a list that allows Iron Man to move left and right according to the direction key |
| move(self, speed)          | object, list    | N/A             | Calculate the speed of the left and right movements differently depending on the angle (speed which is domain of this function is the return value of the turn function.) |
| process(self, speed)       | object, integer | N/A             | A function of the game's progress, the speed here determines the speed of the game. If the game progresses to 100%, the game can be successfully terminated. |

### ObjectClass

| Thread Name                                 | Domain(inputs)           | Range(outputs) | Behavior                                                     |
| ------------------------------------------- | ------------------------ | -------------- | ------------------------------------------------------------ |
| \__init__(self, image_file, location, type) | object, text, list, text | N/A            | Initiate instance variables                                  |
| update(self)                                | object                   | N/A            | Allow the obstacle to move and delete the object when the obstacle is out of the screen |

Q1. Which version of Python did you use to code your project?

python 3.7

Q2. Did you use any Python packages in your project?

Yes, we did. We imported random, sys libraries. These are built-in libraries so you don't need to install them. but you should install a Pygame for joying our project. this link(https://www.pygame.org/wiki/GettingStarted) will guide to install it.