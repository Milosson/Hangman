# HANG MAN 𓍯 

## A SNARE-TASTIC GAME
![Game Img Mockup](/assets/images/pythonsnippet.JPG)

[LIVE LINK FOR THE GAME](https://the-hangman-e57a462a667e.herokuapp.com/)<br>
[GitHub Repo](https://github.com/Milosson/Hangman)
## Project description

Welcome to Hangman game - Snare the Rope Edition.<br>
This Python console-based game brings back the classic to life with a touch of humor and suspense.<br>
Challenge yourself to either guess the secret word letter by letter, or get hung while learning how to spell and guess!

Your are limited with lives based on the choice of difficulty, dare you......?<br>
The used letters will append to remember you how close you are to the gallow! or not...<br>
Victory or defeat, will you triumph or meet a ropey fate?

Lets diiiiive in! It will be a snare-tastic adventure!

## Table of Contents

<details><summary>Click to preview content</summary><br>

- [Features](#features)
  - [Dynamic Hangman Graphics](#dynamic-hangman-graphics)
  - [Difficulty Levels](#difficulty-levels)
  - [Random Word Selection](#random-word-selection)
  - [User Input Validation](#user-input-validation)
  - [Game Over and Victory Screens](#game-over-and-victory-screens)
  - [Menu System](#menu-system)
  - [Clear Screen Functionality](#clear-screen-functionality)
  - [Replay Option](#replay-option)
  - [Main Game Lobby](#main-game-lobby)
  - [Instant Quick Play](#instant-quick-play)
  - [Difficulty Levels as Options](#difficulty-levels-as-options)
  - [Game Description](#game-description)
  - [Winner Screen](#winner-screen)
  - [Game Over Screen](#game-over-screen)
- [Future Features](#future-features)
  - [Multiplayer Mode](#multiplayer-mode)
  - [More Visuals](#more-visuals)
  - [Leaderboard](#leaderboard)
  - [Expand Wordlist](#expand-wordlist)
- [Technologies](#technologies)
- [Testing](#testing)
  - [Automated Validation](#automated-validation)
  - [Manual Testing](#manual-testing)
  - [Fixed Bugs](#fixed-bugs)
  - [Unresolved Bugs](#unresolved-bugs)
  - [Conclusion of Testing](#conclusion-of-testing)
- [Future Code Enhancement](#future-code-enhancements)  
- [Flowchart](#flowchart)
- [Deployment](#deployment)
  - [Heroku Deployment](#heroku-deployment)
  - [GitHub Deployment](#github-deployment)
  - [Forking The GitHub Repository](#forking-the-github-repository)
  - [Cloning the Project](#cloning-the-project)
- [License](#license)
- [Support Information](#support-information)
- [Credits / Acknowledgements](#credits--acknowledgements)
- [Heartfelt Gratitude](#heartfelt-gratitude)
- [Bidding Adieu](#bidding-adieu)

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
 - Python 3.12.2: The core language for implementing game logics in this project<br>
 - GitHub Git version 2.43.2: Version control platform used for hosting and collaborative development.<br>
 - Heroku: Deployment platform for hosting this project.
 - README.md: The markdown file serves as comprehensive documentation, encapsulating essential information about this project <br>
 - Replit and VScode: Used as testing grounds, providing both local and integrated development environment (IDE) testing..
 - Cacoo: Utilized for creating the project's flowchart.
 - Am I Responsive: Creating the the responsive mockups.
 - CI Python Linter: Used for code validation, ensuring adherence to PEP8 standards and maintaining code quality.
 <br><h4><details><summary>Modules</summary>
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
   </details></h4>

## Testing
#### CI Python Linter
Validation through [CI Python Linter](https://pep8ci.herokuapp.com/#)<br>
Initially, I encountered various linter and whitespace issues, which I resolved during local testing and in my IDE. The final result adheres to PEP8 standards, with no errors remaining.
<details><summary> CI-Python Linter Image-1</summary>

![Linter1](/assets/images/linter1.JPG)
</details>
<details><summary> CI-Python Linter Image-2</summary>

![Linter1](/assets/images/linter2.JPG)
</details>
<details><summary> CI-Python Linter Image-3</summary>

![Linter1](/assets/images/linter3.JPG)
</details>
<details><summary> CI-Python Linter Image-4</summary>

![Linter1](/assets/images/linter4.JPG)
</details>
<br>

#### Lighthouse Report

<details><summary>Lighthouse Report</summary>
<h3>The "Best Method" circle bar is affected by an UnloadHandler from the limit-time.js<br>
   *** window.addEventListener('unload', () => { chrome.runtime.onMessage.removeListener(handleExtensionEvents); }); ***
</h3><br>

![Lighthouse](/assets/images/LighthouseHANGMAN1.JPG)

</details>


### Manual Testing

|What was tested|Result|
|---|---|
|Main Loby Menu: Loading. |Passed|
|Spam testing the main loby menu and all the input sections. |Passed|
|Quick play Option 1: Easy mode with 5 lives as an default for quick play. |Passed|
|Select difficulty Option 2: Randomised words should be relevant to the difficulty selected.|Passed|
|Game Description Option 3: Game description with explaination about users choice within difficulty option.|Passed|
|Terminate App Option 4: Should only allow the user to input either, easy, medium, hard, error message if neither of these are selected|Passed|
|Already guessed letters: A message should display to the user that they have already guessed that specific letter|Passed|
|Invalid inputs: Stress tested with invalid inputs, for all sections with input. invalid msg show as excpected|Passed|
|Win / Lose message: A message should display to the user if they have either won or lost the game|Passed|

### Fixed Bugs

|What was tested / Expected results|Actual Results|What was done to fix the bug|
|---|---|---|
|Incrementation on the Hang man drawings |It didn't increment at all |I moved the Hang man graphics to the right section within the codeblock, It didn't get called as expected.|
The clear screen functionality was bugging when tested on macOS|Didn't clear screen at all|By adding varible CC that includes 'posix' else 'cls' for Unix and Windows|

### Unresolved Bugs

| What was tested / Expected results                        | Actual Results                                           | What was done to fix the bug                             |
| --------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| Spamming inputs while the delay time is active on Invalid msgs. | Delayed rendering of Invalid message during spam inputs   | Nothing has been done to fix this issue at the moment.  |
<br>



### 1. First-time User Experience

| **Feature**                        | **Action**                                   | **Expected Result**                         | **Actual Result**                         |
| -----------------------------------| ---------------------------------------------| ------------------------------------------| ----------------------------------------|
| Increase delay for invalid input    | User encounters invalid input                | Improved delay for better user experience  | Works as expected                         |

### 2. Improved Text Display

| **Feature**                        | **Action**                                   | **Expected Result**                         | **Actual Result**                         |
| -----------------------------------| ---------------------------------------------| ------------------------------------------| ----------------------------------------|
| Increase delay for info text        | User encounters info text                    | Improved delay for better user experience  | Works as expected                         |

### 3. Visual Output and Text Enhancement

| **Feature**                        | **Action**                                   | **Expected Result**                         | **Actual Result**                         |
| -----------------------------------| ---------------------------------------------| ------------------------------------------| ----------------------------------------|
| Display and align text and color    | Scuffed coloring and text without alignment | Better-optimized color scheme and less clutter  | Works as expected                   |

### 4. User-Requested Replay Button

| **Feature**                        | **Action**                                   | **Expected Result**                         | **Actual Result**                         |
| -----------------------------------| ---------------------------------------------| ------------------------------------------| ----------------------------------------|
| Display Replay Button               | User requests a replay option                | Replay button displayed for better user experience | Works as expected                   |

### 5. Winner Screen Addition

| **Feature**                        | **Action**                                   | **Expected Result**                         | **Actual Result**                         |
| -----------------------------------| ---------------------------------------------| ------------------------------------------| ----------------------------------------|
| Winner Screen                       | User requests a winner screen at the end     | Winner screen displayed for a celebratory end of the game | Works as expected                   |
### 6. Color scheme

| **Feature**                        | **Action**                                   | **Expected Result**                         | **Actual Result**                         |
| -----------------------------------| ---------------------------------------------| ------------------------------------------| ----------------------------------------|
| Throughout Color scheme     | User request to have a more throughout color in the app    | More visually appealing color scheme | Works as expected                   |

<details><summary>Conclusion of Testing</summary>

The testing phase for the Hangman - Snare the Rope Edition project was thorough, covering functionality, user experience, and bug resolution. Both automated validation through the CI Python Linter and manual testing were employed to ensure a stable and error-free gaming experience.

The testing process significantly contributed to refining the project, resulting in a stable, user-friendly, and entertaining gaming experience.

### Future Considerations
The testing phase provided valuable insights, leading to potential future improvements:

- **Bug Resolution:** Addressing the unresolved bug related to spamming inputs.
- **User Interface Enhancements:** Continuously improving visual and interactive elements for an enhanced gaming experience.
- **Feature Additions:** Exploring opportunities to add multiplayer mode, more visuals, a leaderboard, and an expanded wordlist.

</details>

<details><summary>Future Code Enhancements</summary>

In future iterations of the project, I plan to enhance the codebase by incorporating more robust exception handling syntax. Additionally, I intend to refactor the main game loop, 'hangmanthegame', into smaller, well-organized sections. This restructuring aims to improve readability and maintainability, making it easier for both assessors and myself to comprehensively test different functions.

I identified the need for these improvements during manual testing, realizing that a more structured approach would enhance the overall quality and understandability of the code.

</details>


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

## Credits / Acknowledgements

Initially, I found myself at a crossroads, uncertain about the direction to take for this project. A special thanks to @GarethMcGirr, my mentor, who provided valuable guidance during our session, helping me navigate through different options.

### Code 
- The foundation of my project draws inspiration from various sources within the coding community. I owe gratitude to multiple channels and platforms, including Slack and my peers, whose previous submissions served as a wellspring of inspiration, guiding me to carve my own path.
>
  * *[Code Institute](https://codeinstitute.net/) - The main source of knowledge used to create this project.*
      * *[Love Sandwiches](https://github.com/Milosson/love-sandwiches) - The initial Python project in collaboration with school provided the confidence to apply the acquired knowledge.*
  * *[Stack Overflow](https://stackoverflow.com/search?page=3&tab=Relevance&pagesize=15&q=hangman%20python&searchOn=3) - A valuable forum where I found solutions and insights related to Hangman in Python.*
  * *[Stack Exchange](https://stackexchange.com/search?q=hangman+python) - Another resourceful forum on Hangman in Python, where I encountered and resolved common errors and issues.*
  * *[MakeUseOf](https://www.makeuseof.com/python-game-hangman-create/?utm_source=flipboard&utm_content=topic%2Fadventuregame) - Another resourceful website that proved useful for comparison and logic implementation.*
  * *[Unga Programmerare](https://www.youtube.com/watch?v=fB4Yp72ngR4&t=479s&ab_channel=UngaProgrammerare) - A YouTube channel that provided insights into game logic, presented in my native language.*
  * *[Kite](https://www.youtube.com/watch?v=m4nEnsavl6w&ab_channel=Kite) - Another YouTube channel, Kite, was instrumental in cross-comparing game logics and understanding general code structures.*
  * *[ANSI Escape](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal/7839185#7839185) - Inspiration for the ANSI Escape.* 

### Heartfelt Gratitude

I would like to express my sincere gratitude to one of the most exceptional Slack communities I've had the privilege of being a part of - **[CODEINSTITUTE](https://codeinstitute.net/)**. The community is filled with dedicated **peers**, **mentors**, and **tutors** who have made the coding journey, with all its challenges and moments of progression, incredibly rewarding.

Special thanks to the following individuals:

**My Dad(Hadi Razzaz):** Serving as both a first-time user of the app and an advisor, he brings a wealth of experience as a working systems specialist with many years in the field. His insights and guidance have been crucial in shaping my progress.

**Samson:** A first-time user of the app who provided valuable feedback during a Discord meeting.

**Syllet:** Another first-time user of the app who shared feedback in collaboration with Samson during a joint meeting.

**Nabz:** An advisor and guide with an iron fist, directing me to the right forums, providing constructive criticism, and serving as both a tester and a first-time user.

Your insights and contributions have been invaluable. Thank you for being a part of this journey!


## Bidding Adieu

```  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
Hang tight!𓍯 I'll be back with more code-tastic adventures🪂 and witty banter before you know it! Until then, may your variables be well-defined, and your algorithms run with the grace of a well-optimized function. Catch you on the flip side! 👨🏻‍💻👩🏻‍💻
