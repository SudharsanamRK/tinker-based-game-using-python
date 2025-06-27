# Tkinter-Based Color Game

## Project Summary

This is a simple color-matching brain game built using Python and Tkinter. The objective is to type the **font color** of a displayed word—not the word itself—within a limited time. It sharpens focus and reflexes.

---

## How It Works

- A color name (e.g., "Red") is shown in a random font color (e.g., green).
- The player must type the **font color** (in this case, "green").
- The game includes:
  - Timer-based gameplay
  - Score tracking
  - Difficulty levels (Easy, Medium, Hard)
  - Sound feedback on correct answers
  - High score storage in a file

---

## Requirements

- Python 3.x
- Tkinter (built-in with Python)
- playsound module for sound:

```bash
pip install playsound==1.2.2
```

---

## How to Run

Open terminal and run:

```bash
python color_game.py
```

Or:

```bash
py color_game.py
```

---

## Files Included

| File           | Description                          |
|----------------|--------------------------------------|
| `color_game.py` | Main Python script                   |
| `highscore.txt` | Stores high score locally            |
| `ding.mp3`      | (Optional) Sound on correct answers  |
| `README.md`     | Project documentation                |

---

## Features

- Real-time color challenge
- Timer countdown
- High score persistence
- Reset and difficulty controls
- Sound effects (optional)

---

## Output
![Game Preview](output-gif.gif)

---
