# Tic-Tac-Toe AI with Min-Max Algorithm

## Overview
This project implements an AI-powered Tic-Tac-Toe game using the Min-Max algorithm. The AI makes optimal moves, ensuring an unbeatable opponent.

## Features
- Single-player mode against AI
- Min-Max algorithm for optimal decision-making
- Simple and interactive CLI-based interface
- Supports 3x3 Tic-Tac-Toe grid

## How It Works
1. The game alternates turns between the player and the AI.
2. The AI evaluates possible moves using the Min-Max algorithm.
3. The AI selects the best move to maximize its chances of winning.
4. The game continues until there is a winner or a draw.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Aditya-Ranjan1234/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
   ```
2. Run the Python script (ensure Python is installed):
   ```sh
   python tic_tac_toe.py
   ```

## Usage
- Follow on-screen instructions to play.
- The player selects a position (1-9) to make a move.
- The AI responds optimally using the Min-Max algorithm.

## Algorithm Explanation
The Min-Max algorithm works as follows:
- It recursively explores all possible game states.
- It assigns a score to each state: +10 for AI wins, -10 for player wins, and 0 for draws.
- The AI selects the move that maximizes its minimum guaranteed score.

## Example Game
```
Player (X) - AI (O)
 1 | 2 | X 
---+---+---
 O | X | O 
---+---+---
 X | O | X 
```
Result: Draw
