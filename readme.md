
# Snake Game

This is a classic Snake game developed using Python and Pygame. The game features different modes, power-ups, obstacles, and a scoring system including high scores.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Editing the Code](#editing-the-code)
- [Developer](#developer)

## Features

- Multiple difficulty modes with varying grid sizes
- Realistic snake appearance and apple design
- Power-ups and obstacles
- High score tracking
- Game Over screen with option to replay or quit

## Requirements

- Python 3.x
- Pygame 2.6.0

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/minggudev/snake-game.git
    cd snake-game
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the game, run the following command:
```sh
python main.py
```

### Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **C**: Play again (on Game Over screen)
- **Q**: Quit the game (on Game Over screen)

## Code Structure

The project is organized as follows:

```
snake-game/
│
├── main.py          # Main game loop and game over screen
├── settings.py      # Game settings and constants
├── snake.py         # Snake class implementation
├── food.py          # Food class implementation
├── powerups.py      # Power-ups class implementation
├── obstacles.py     # Obstacles class implementation
├── score.py         # Score management
├── requirements.txt # Project dependencies
```

## Editing the Code

### Adding New Features

To add new features, follow these steps:

1. **Clone the repository** (if you haven't already):
    ```sh
    git clone https://github.com/minggudev/snake-game.git
    cd snake-game
    ```

2. **Create a new branch** for your feature:
    ```sh
    git checkout -b feature-name
    ```

3. **Edit the necessary files** to implement your feature. Make sure to follow the existing code structure and naming conventions.

4. **Commit your changes** with a meaningful commit message:
    ```sh
    git commit -m "Add feature: description of the feature"
    ```

5. **Push the branch** to your GitHub repository:
    ```sh
    git push origin feature-name
    ```

6. **Create a pull request** on GitHub to merge your feature branch into the main branch.

### Modifying Existing Code

1. **Open the file** you want to modify in your preferred code editor.

2. **Make the necessary changes**. Ensure your code follows the project's style and guidelines.

3. **Test the game** to ensure your changes work correctly:
    ```sh
    python main.py
    ```

4. **Commit your changes** with a clear commit message:
    ```sh
    git commit -m "Fix/Update: description of the change"
    ```

5. **Push your changes** to your GitHub repository:
    ```sh
    git push
    ```

## Developer

This project is maintained by [minggudev](https://github.com/minggudev). Feel free to reach out for any questions or suggestions.

---