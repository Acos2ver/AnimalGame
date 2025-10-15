# AnimalGame

A Python implementation of an abstract strategy board game featuring object-oriented design and custom movement mechanics.

## About

AnimalGame is a two-player turn-based strategy game built to demonstrate proficiency in object-oriented programming, game logic implementation, and software design patterns. The game features a 7×7 grid with four unique piece types, each with distinct movement rules.

## Key Features

- **Object-oriented architecture** with inheritance hierarchy for game pieces
- **Movement validation system** handling sliding, jumping, and capture mechanics
- **Turn-based game logic** with state management and win condition tracking
- **Algebraic notation** for board position references (e.g., 'a1', 'g7')

## Technical Implementation

### Game Pieces

| Piece | Movement Type | Distance | Behavior |
|-------|--------------|----------|----------|
| Chinchilla | Diagonal | 1 square | Sliding |
| Wombat | Orthogonal | 4 squares | Jumping |
| Emu | Orthogonal | 3 squares | Sliding |
| Cuttlefish | Diagonal | 2 squares | Jumping |

- **Sliding pieces**: Move up to their distance but can be blocked
- **Jumping pieces**: Move exactly their distance and cannot be blocked
- All pieces can move 1 square in their alternate direction (diagonal ↔ orthogonal)

### Class Structure
```
Piece (Abstract Base)
├── Chinchilla
├── Wombat
├── Emu
└── Cuttlefish

AnimalGame (Game Controller)
```

## Usage
```python
from AnimalGame import AnimalGame

# Initialize game
game = AnimalGame()

# Execute moves
game.make_move('c1', 'c3')  # Tangerine player
game.make_move('e7', 'e5')  # Amethyst player

# Check game state
status = game.get_game_state()  # Returns: 'UNFINISHED', 'TANGERINE_WON', or 'AMETHYST_WON'
```

## Core Methods

- `get_game_state()` - Returns current game status
- `make_move(from_square, to_square)` - Validates and executes moves
  - Checks turn order, piece ownership, and move legality
  - Returns `True` if successful, `False` otherwise

## Design Principles

- **Encapsulation**: All data members are private
- **Inheritance**: Piece classes inherit from base `Piece` class
- **Validation**: Comprehensive move validation and error handling
- **State Management**: Tracks player turns, piece positions, and win conditions

## Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

- Python 3
- Object-Oriented Programming (OOP)

## Skills Demonstrated

- Class design and inheritance
- Algorithm implementation (movement validation)
- Game state management
- Unit testing and debugging
- Clean code practices

---

**Project Type**: Academic | **Language**: Python | **Focus**: Object-Oriented Design
