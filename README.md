# Connect4AI

***A comprehensive Connect Four suite built in Python with Pygame. This repository demonstrates the evolution of game logic from a standard two-player local game to an advanced AI-driven experience.***
  

## Game Modes

 - Two-Player Mode (connect4.py) : This is the classic local multiplayer version.
      - **Format**: Player 1 vs. Player 2.
      - **Controls:** Mouse-controlled movement and clicking to drop pieces.
      - **Goal:** A perfect way to test the core mechanics and UI before diving into AI logic.
   
 - AI Mode (connect4_with_ai.py): The advanced version featuring an intelligent digital opponent.
   - **Format:** Human Player vs. AI.
   - **Algorithm:** Powered by a Minimax Algorithm utilizing NumPy for efficient board state evaluations.
   - **Intelligence:** The AI calculates the optimal move by looking ahead at potential board states, prioritizing center-column control, and blocking immediate threats.

## Installation & Setup

### Prerequisites

Ensure you have Python 3.x installed.
1. Clone the Repository 

> git clone https://github.com/pranayagarwal7/Connect4AI.git 

> cd Connect4AI

2. Install Dependencies

> pip install -r requirement.txt

### How to Run

**Play with a friend (Local PvP):**

> python3 connect4.py

**Challenge the AI (PvE):**

> python3 connect4_with_ai.py

## Technical Deep Dive

 - **Graphics:** Rendered using Pygame for a smooth, responsive 60 FPS experience.
   
 - **AI Logic:** The AI doesn't just play randomly; it uses a scoring system to evaluate every possible move. It assigns weights to   
   sequences (e.g., a "3-in-a-row" is weighted heavily to prioritize a  
   win or a block).
   
 - **Data Management:** NumPy matrices are used to represent the 6x7 board, allowing for rapid row/column/diagonal slicing during   
   win-check calculations.

## Technologies Used

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pygame](https://img.shields.io/badge/pygame-black?style=for-the-badge&logo=pygame&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

</div>

## Skills & Logic

<div align="center">
  
![Minimax Algorithm](https://img.shields.io/badge/Algorithm-Minimax-red?style=for-the-badge&logo=google-cloud&logoColor=white)  ![Game Development](https://img.shields.io/badge/Domain-Game%20Dev-orange?style=for-the-badge&logo=unity&logoColor=white) ![Matrix Operations](https://img.shields.io/badge/Math-Matrix%20Operations-blue?style=for-the-badge&logo=spreadsheet&logoColor=white) ![Data Structures](https://img.shields.io/badge/CS-Data%20Structures-green?style=for-the-badge&logo=codeforces&logoColor=white)

</div>

## License

This project is licensed under the MIT License.


## Verdict: The AI is tough! I've only won 3 out of 10 games—think you can do better?

