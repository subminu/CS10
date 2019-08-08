Eunbin Seo, 3035255510, TA Andrew Burke

Minwoo Choi, 3035272150, TA Andrew Burke

# <center>Iron Man VS Thanos</center>

### Preface

Q1. Which version of Python did you use to code your project?

python 3.7

Q2. Did you use any Python packages in your project?

Yes, we did. We imported random, sys libraries. These are built-in libraries so you don't need to install them. but you should install a Pygame for enjoying our project. this link(https://www.pygame.org/wiki/GettingStarted) will guide to install it.

Q3. How to implement this?

If you are familiar with git, follow this instruction(https://help.github.com/en/articles/cloning-a-repository). This is our git hub address: https://github.com/subminu/CS10. 

If you're not, please download file(zip) from here(https://drive.google.com/open?id=11c5UCwRw_e-U3ZlY40Ci01jKvShErPWP)

Then open the terminal in the directory which include our file and command this.

> python ThanosVSIronMan.py

If it does not work, try this.

> python3 ThanosVSIronMan.py

## Introduction 

1. ##### What is your vision for the project at a high level?

   We made a “Iron Man VS Thanos” that Iron Man avoids attacks(meteoroids) of Thanos and charges energy.

2. ##### How will someone use your project?

   The keyboards that are “left arrow, right arrow” make Iron Man turn and move left and right.

3. ##### What are two/three specific features you want to build?

   We created an object through the **\<Class>** function. Here’s what this object does:

   * Game Environment - We made game screens of the beginning and the end of the game. Also, we created the scroll under the screen. The scroll shows how close Iron Man is to Thanos.

   * Objects -  Items(Arc reactors) and attacks(meteoroids) fall from the top randomly. The difficulty level was adjusted by dividing the first position of Iron Man and the position of the Thanos by 4. We created a probability to increase the number of meteoroids as the stages go up. In other words, The closer Iron Man got to Thanos, the more attacks(meteoroids) are created. It is easier to avoid meteoroids and get items in the first stage than the fourth stage. 

   * Stamina of Iron Man - We created instance variables to manage Iron Man’s stamina(heart). If Iron Man runs out of stamina of Iron Man reaches the Thanos, the game is over. And Iron Man’s life increases if the Iron Man obtains 10 the Arc reactors. In other words, life increases when the score is more than 100. Three lives are maximum. We can see how many lives are left on the upper right screen.

## Details

1. ##### How our project works? (Algorithm)

   * Thanos A.I: The basic algorithm is a random attack using a random library. This algorithm does not change even if the phase is changed. but more objects and more meteoroids them will be generated. it makes the difficulty increasingly difficult. There are four levels in total, and the ratio of meteoroid and energy for each phase was divided into 1: 1, 2: 1, 3: 1, 4: 1.
   * Score system: When Iron Man gets the Arc reactors, the score increases by 10 points. If Iron Man is attacked by Thanos, it is reduced by 50 points. If there are less than three hearts and score is more than 100 points, the heart is automatically filled. For the total score, the hearts are converted to 100 points.

2. ##### What is your purpose of the various lists?

   * List of Iron Man png files ( IronMan_images)

     We put Iron Man’s five states on the list. Whenever Iron Man turn and move through direction keys, we have to change Iron Man’s png files. So, we use the list(that is arranged in order of front, right1, right2, left2, left1) to change the  Iron Man’s images. When the right key is pressed, the index increases 1. (When the left key is pressed, the index decreases 1.)

   * Speed list (speed = [self.angle, 10 - abs(self.angle)*2], this list is in “turn” method of **\<IronManClass>**.) 

     We store the degree of turning in instance variable(angle). We can change the speed according to the degree of turning by using the list.	

   * Position list

     We bundle up x position and y position by using list. This list is a single list can describe the location of texts or images that display on the screen.

   * Probability list (types=[“meteoroid”]*(1+level)+[“power”] in “create_map” function)  

     The reason why we were able to change the probability of Thanos’ attack was because we used this list.

3. **What is your purpose of the local(or instance) variables?**

   * IronMan.heart

     An instance variable of the Iron Man class, which is an important factor in determining the game's winning or losing.

   * result

     a local variable, which is parameter of *show_game_over(result)*

     If all of the heart(IronMan.heart) is losed after being attacked by the Thanos, the result is to receive the text "Lose" and display the corresponding loss_text on the screen.
     Conversely, if the heart reaches the Thanos, the result is to receive the text "Win" and display the corresponding win_text on the screen.

   * scroll

     a local variable, which is parameter of *animate(scroll)*

     This parameter(boolean) determines the speed of the Iron Man displayed at the bottom of the game screen. If the value of this variable is true as boolean, run the process function so that the Iron Man at the bottom of the game screen can move.

   * damage

     a local variable, which is parameter of *show_stamina(self,damage)*

     Local variable with boolean value. If the value is true, the IronMan.heart value is reduced to 1 and the number of hearts seen on the game screen is also reduced by one.

     

## Functions & Thread

### Main

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
| turn(self, direction)*     | object, integer | list(speed)     | Returns a list that allows Iron Man to move left and right according to the direction key |
| move(self, speed)*         | object, list    | N/A             | Calculate the speed of the left and right movements differently depending on the angle (speed which is domain of this function is the return value of the turn function.) |
| process(self, speed)       | object, integer | N/A             | A function of the game's progress, the speed here determines the speed of the game. If the game progresses to 100%, the game can be successfully terminated. |

\* These functions are coded by reference. 

### ObjectClass

| Thread Name                                 | Domain(inputs)           | Range(outputs) | Behavior                                                     |
| ------------------------------------------- | ------------------------ | -------------- | ------------------------------------------------------------ |
| \__init__(self, image_file, location, type) | object, text, list, text | N/A            | Initiate instance variables                                  |
| update(self)                                | object                   | N/A            | Allow the obstacle to move and delete the object when the obstacle is out of the screen |

## Reference

Our project was created with inspiration from Skier game(https://github.com/SentinelWarren/Skier-Game/blob/master/Skier.py), a sample game that is basically provided by Pygame. 