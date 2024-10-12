# Kids Game

A simple interactive game for kids using Pygame and natural language processing with spaCy.

## Description

This project is a Pygame-based interactive game designed for children. It features a character that can be controlled using natural language commands. The game processes these commands using the spaCy NLP library, allowing for an intuitive and educational gaming experience.

## Features

- Interactive character movement using natural language commands
- Character color changing functionality
- Jumping mechanism
- Background image display
- Text input for command processing

## Requirements

- Python 3.x
- Pygame
- spaCy
- spaCy English language model (en_core_web_sm)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/kids-game.git
   cd kids-game
   ```

2. Install the required packages:
   ```
   pip install pygame spacy
   ```

3. Download the spaCy English language model:
   ```
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Ensure you have an `assets` folder in the same directory as the script, containing a `pattern.jpg` file for the background.

2. Run the game:
   ```
   python kids_game.py
   ```

3. Use the following commands in the input box:
   - "Move left/right/up/down": Moves the character in the specified direction
   - "Jump": Makes the character jump
   - "Change color": Changes the character's color randomly

## Controls

- Type commands in the input box at the bottom of the screen
- Press Enter to submit a command
- Use Backspace to delete characters in the input box

## Acknowledgements

- [Pygame](https://www.pygame.org/)
- [spaCy](https://spacy.io/)
