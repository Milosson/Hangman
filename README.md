# HANG MAN 𓍯 

## A SNARE-TASTIC GAME
![Game Img Mockup](/assets/pythonsnippet.JPG)

## Project description

Welcome to Hangman game - Snare the Rope Edition.<br>
This Python console-based game brings back the classic to life with a touch of humor and suspense.<br>
Challenge yourself to either guess the secret word letter by letter, or get hung while learning how to spell and guess!

Your are limited with lives based on the choice of difficulty, dare you......?<br>
The used letters will append to remember you how close you are to the gallow! or not...<br>
Victory or defeat, will you triumph or meet a ropey fate?

Lets diiiiive in! It will be a snare-tastic adventure!

<h2>Table of Contents</h2><br>
<details><summary><span style="background-color: #0000FF">Click to preview content</span></summary><br>

* Features
 - Future features
* Techonologies used
* Testing
* Flowchart
* Deployment
* Support information
* Credits / Acknowledgements
* License
* Bidding Adieu / Conclusion

</details>

## Features

### Dynamic Hangman Graphics
- **Experience:** Dynamic hangman graphics that adapt based on the number of lives remaining.
- **Enhancement:** Visual elements enhance the overall gaming experience.

### Difficulty Levels
- **Choose Your Challenge:** Three difficulty settings - Easy, Medium, and Hard.
- **Variety:** Each difficulty level offers a unique set of word length and lives accordingly.

### Random Word Selection
- **Unpredictability:** Unpredictability in the random word choice keeps each gameplay fresh and exciting.

### User Input Validation
- **Valid Inputs:** Ensure your inputs are valid, allowing only single letter entries.
- **Feedback:** Receive helpful feedback if an invalid input is provided.

### Game Over and Victory Screens
- **Visual Appeal:** Experience visually appealing ASCII art at the end of each gameplay.

### Menu System
- **Navigation:** Navigate through different options using the built-in menu system.
- **Options:** Choose between quick play, difficulty selection, accessing game information, or terminating the app.

### Clear Screen Functionality
- **Maintain Clean Display:** Maintain a clean display throughout the game with screen-clearing.
- **Visual Enhancement:** Enhancing the overall visual feeling during various stages.

### Replay Option
- **Seamless Experience:** Seamless gameplay experience without restarting the app.

##
### Main Game Lobby
<details>
  <summary>Main Game Lobby</summary>

  - **Warm Welcome:** Upon launching the game, users are greeted with a warm welcome message.
  - **Engaging Menu:** The game menu is presented to set the tone for an engaging gaming experience.

  ![Hangman Lobby](/assets/images/hangman-start-main.JPG)

</details>

### Instant Quick Play

<details>
  <summary>Instant Quick Play</summary>

  - **Spontaneous Gaming:** Option for a spontaneous gaming experience at the start with the quick play function.
  - **Jump Into Action:** Allows the user to jump straight into the action without extensive setup.

  ![Quick Play](/assets/images/hangman-opt1-easy.JPG)

</details>

### Difficulty Levels as Options

<details>
  <summary>Difficulty Levels as Options</summary>

  - **Choose Your Challenge:** Choose from multiple difficulty levels, including Easy, Medium, and Hard.
  - **Tailored Experience:** Tailor the gaming experience to your preferred level of challenge.

  ![Difficulty Options](/assets/images/hangman-diffoption.JPG)

</details>

### Game Description

<details>
  <summary>Game Description</summary>

  - **Classic Hangman:** Dive into the classic Hangman game with a touch of humor and suspense.
  - **Console Interface:** Brought to life through a console-based interface.

  ![Game Description](/assets/images/hangman-gamedescription.JPG)

</details>

### Winner Screen

<details>
  <summary>Winner Screen</summary>

  - **Celebratory Display:** A celebratory display congratulating you on successfully guessing the word.

  ![Winner Screen](/assets/images/hangman-winner.JPG)

</details>

### Game Over Screen
<details>
  <summary>Game Over Screen</summary>

  - **Defeat Visuals:** Illustrations reflecting the game-over scenario.
  
  - **Replay Option:** Don't worry! We have a replay function ready for you ❤️.

  ![Game Over](/assets/images/hangman-gameover.JPG)
  
</details>

## Future Features

### Multiplayer Mode
- **Real-time Battles:** Challenge your friends or other players in real-time battles.

### More Visuals
- **Enhanced Experience:** Enhance the visual experience with additional graphics and more aligned, structured graphics.

### Leaderboard
- **Competitive Spirit:** Compete for the top spot and compare your Hangman skills with others.

### Expand Wordlist
- **Regular Updates:** Expand and update the wordlist regularly for a continuously enriching gameplay experience.


## Technologies
 - Python 3.12.2 - Game logics core language for this project<br>
 - GitHub Git version 2.43.2 - Version control platform for hosting the project.<br>
 - Heroku - Deployment platform for this project.
 - README.md - The markdown file including all project documentations.<br>
 - Replit and VScode as testing ground both local and IDE.
 - Cacoo for flowchart
 - Am I Responsive for the mockups.
 - CI Python Linter for validation of code.
 <br><details><summary>Modules</summary>
   - random<br>
   - os<br>
   - string<br>
   - time<br>
   - Wordlist.py
      * easy_words
      * medium_words
      * hard_words
      * logo
      * graphics
      * gamedescriptions
      * endgamevis
      * winnerlogo
      * TxtColor=(RC,GC,YC,RS)
   </details>

## Testing
ADD TESTING

## Flowchart
<details><summary>Flowchart</summary>

![Flowchart image](/assets/images/Flowchart1.png)

</details>

## Deployment 
<details><summary>Heroku Deployment</summary><br>

i. Create or log in to your account at [Heroku](www.heroku.com).

ii. Click 'New' -> 'Create new app'.

iii. Type in the app name (the-hangman) -> select the region -> 'Create app'.

iv. Navigate to the 'Settings' tab.

v. Click 'Reveal Config Vars' -> Add key: 'PORT' and value: '8000'.

vi. Click 'Add buildpack' -> add 'python' (for Python) and 'nodejs' (for Node.js).
#### It is crucial that the order of buildpacks are as mentioned: 1(Shown as first) 'Python' and 2(Second) 'Nodejs'.

vii. Navigate to the 'Deploy' tab.

viii. Select 'GitHub' in the 'Deployment method' area.

ix. Enter the GitHub repository name in the search bar -> 'Connect'.

x. Click 'Deploy Branch' and wait for the build to complete.

</details><br>

<details><summary>GitHub Deployment</summary><br>


i. Log into your GitHub account.<br>

ii. Navigate to the repository (milosson/Hangman).<br>

iii. Click on the 'Settings' option at the top of the repository.<br>

iv. Select 'Pages' from the left-hand menu, located near the bottom.<br>

v. Within the 'Source' tab, select the drop-down titled 'None'.<br>

vi. Choose the branch named 'main' (in some cases, it can be named 'Master').<br>

vii. Click 'Save'.<br>

viii. You will be prompted with a URL to your deployed site.<br>

ix. Your site is now deployed. Please note that it might take a moment for the URL to update. Refresh the page until the site is fully deployed. 
</details><br>

<details><summary>Forking The GitHub Repository</summary><br>


i. Log into your GitHub account.<br>

ii. Navigate to the repository you are willing to fork (milosson/Hangman).<br>

iii. In the upper-right of the repository, click the 'Fork' button.<br>

iv. A copy of the repository will now be available within your repositories.<br>

v. You now have a copy of the code available to clone and work on without affecting the original code.
</details><br>

<details><summary>Cloning the Project</summary>

To make a local clone of the project, follow these steps:

i. Log into your GitHub account.<br>

ii. Navigate to the repository (the-hangman).<br>

iii. In the upper section of the repository, click the drop-down named 'Code'.<br>

iv. Copy the SSH address (`git@github.com:Milosson/Hangman.git`).<br>

v. Open GitBash.<br>

vi. Navigate to the correct directory.<br>

vii. Create a new directory named 'the-hangman-clone'.<br>

viii. CD into 'the-hangman-clone'.<br>

iv. Enter `git clone git@github.com:Milosson/Hangman.git`.<br>

x. GitBash will clone the repository into this directory.<br>

xi. Enter `code .`.
</details><br>

 

## License
<details><summary><span style="background-color: #0000FF">MIT License</span></summary>

Copyright (c) [2024] [Milo Razzaz]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.</details>

## Support Information

For any issues or inquiries, please contact [ milorazzaz@protonmail.com ]

## Credits

ADD CREDITS 

## Acknowledgements

ADD ACKNOWLEDGEMENTS

## Bidding Adieu

Hang tight! ;) I'll add some vitty heereee soon!
