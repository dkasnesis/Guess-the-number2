🎲 Guess The Number Game

  
  



  A fun and interactive number-guessing game built with Python and Tkinter! 🎮


🌟 Overview
"Guess The Number" is an engaging game where players select a difficulty level and try to guess a randomly generated number. With intuitive visual feedback and a sleek dark-themed interface, players can test their guessing skills while tracking their attempts.
✨ Features

Multiple Difficulty Levels:
🟢 Easy: Guess a number between 0 and 50
🟡 Normal: Guess a number between 0 and 100
🔴 Hard: Guess a number between 0 and 500


Visual Feedback: Up/down arrows and a checkmark guide your guesses
Try Counter: Keep track of your attempts
User-Friendly Interface: Dark-themed UI with clear instructions
Keyboard Support: Press "Enter" to submit guesses
Interactive Controls: Buttons for randomizing numbers and exiting the game

📋 Requirements

Python 3.x
Tkinter (included with standard Python installations)
Image files: uparrow.png, downarrow.png, correct.png, dice.png (must be in the same directory or bundled with PyInstaller)

🚀 Installation

Clone the repository:git clone https://github.com/your-username/guess-the-number.git


Place the required image files (uparrow.png, downarrow.png, correct.png, dice.png) in the same directory as the script.
Run the game:python guess_the_number.py



🎮 How to Play

Start the game by running the script.
Choose a difficulty level using the radio buttons (Easy, Normal, or Hard).
Click Randomize to generate a secret number.
Enter your guess in the text box and press Enter.
Follow the visual cues:
⬆️ Up Arrow: Your guess is too low
⬇️ Down Arrow: Your guess is too high
✅ Checkmark: You guessed correctly!


Monitor your attempts with the try counter.
Click Exit to close the game.

🖼️ Screenshots
(Add screenshots of your game here for a visual preview!)
💡 Notes

The game uses resource_path to ensure image compatibility when bundled with PyInstaller.
The window is fixed at 300x310 pixels with a stylish dark theme.
The "Enter" key is bound for quick guess submission.

📜 License
This project is licensed under the MIT License - see the file for details.
🙌 Acknowledgments

Built with ❤️ using Python and Tkinter
Inspired by classic number-guessing games



  Happy Guessing! 🎉
