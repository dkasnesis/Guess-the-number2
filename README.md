Guess The Number Game

Description

"Guess The Number" is a simple Python game built using the Tkinter library. The player selects a difficulty level and tries to guess a randomly generated number within a specified range. The game provides visual feedback (up/down arrows or a correct sign) to guide the player and tracks the number of attempts.

Features





Three difficulty levels:





Easy: Guess a number between 0 and 50



Normal: Guess a number between 0 and 100



Hard: Guess a number between 0 and 500



Visual feedback with images (up arrow, down arrow, correct sign)



Tracks the number of tries



User-friendly interface with a dark theme



Press "Enter" to submit guesses



Buttons to randomize the number and exit the game

Requirements





Python 3.x



Tkinter (usually included with Python)



Image files (uparrow.png, downarrow.png, correct.png, dice.png) in the same directory as the script or bundled with PyInstaller

Installation





Clone the repository:

git clone https://github.com/your-username/guess-the-number.git



Ensure the required image files (uparrow.png, downarrow.png, correct.png, dice.png) are in the same directory as the script.



Run the game:

python guess_the_number.py

Usage





Launch the game by running the script.



Select a difficulty level using the radio buttons (Easy, Normal, or Hard).



Click the "Randomize" button to generate a secret number.



Enter your guess in the text box and press "Enter" to submit.



Use the visual feedback (up arrow for too low, down arrow for too high, checkmark for correct) to refine your guess.



The number of tries is displayed on the screen.



Click "Exit" to close the game.

Screenshots

(Optional: Add screenshots of the game interface here)

Notes





The game uses resource_path to handle image loading when bundled with PyInstaller, ensuring compatibility with executable files.



The game window has a fixed size of 300x310 pixels and a dark theme for better visuals.



The "Enter" key is bound to the guess-checking function for convenience.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments





Built with Python and Tkinter



Inspired by classic number-guessing games
