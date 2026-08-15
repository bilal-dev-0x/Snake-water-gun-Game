<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,45:7C3AED,100:0EA5E9&height=170&section=header&text=Snake%20Water%20Gun&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=A%20clean%20Python%20CLI%20logic%20game%20based%20on%20simple%20winning%20rules&descSize=14&descAlignY=56" alt="Snake Water Gun banner" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Type-CLI%20Game-2563EB?style=for-the-badge" alt="CLI Game" />
  <img src="https://img.shields.io/badge/Focus-Rule%20Based%20Logic-7C3AED?style=for-the-badge" alt="Rule based logic" />
  <img src="https://img.shields.io/badge/Level-Beginner-22C55E?style=for-the-badge" alt="Beginner" />
  <img src="https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge" alt="MIT License" />
</p>

---

## Overview

Snake Water Gun is a beginner-friendly Python command-line game inspired by Rock Paper Scissors. The player chooses one option, the computer chooses randomly, and the result is decided through a simple rule table.

The project is intentionally small, but it shows clean beginner logic with dictionaries, tuples, random choices, conditionals, and input validation.

---

## Game Rules

| Choice | Beats | Loses To |
|---|---|---|
| Snake | Water | Gun |
| Water | Gun | Snake |
| Gun | Snake | Water |

If both choices are the same, the match is a draw.

---

## How To Play

| Input | Meaning |
|---|---|
| `s` | Snake |
| `w` | Water |
| `g` | Gun |

---

## Project Structure

```text
Snake-water-gun-Game/
|-- Snake-water-gun.py
|-- LICENSE
`-- README.md
```

---

## How To Run

```bash
git clone https://github.com/bilal-dev-0x/Snake-water-gun-Game.git
cd Snake-water-gun-Game
python Snake-water-gun.py
```

---

## Example Output

```text
Snake Water Gun Game
Choose one: s for snake, w for water, g for gun
Enter your choice: s
Computer chose: water
You chose: snake
Snake beats water.
You win!
```

---

## Concepts Practiced

| Concept | Practice |
|---|---|
| Randomization | Computer choice with `random.choice()` |
| Dictionaries | Mapping shortcut input to full choice names |
| Tuples | Storing winning pairs cleanly |
| Conditionals | Deciding win, lose, or draw |
| Input validation | Handling invalid user choices |
| Game rules | Representing simple logic in code |

---

## Future Improvements

- Add score tracking.
- Add best-of-3 mode.
- Add replay without restarting the script.
- Add difficulty or streak mode.
- Convert the game into a GUI version.

---

<p align="center">
  <b>A small Python logic game with clean rules, readable code, and beginner-friendly structure.</b>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0EA5E9,50:7C3AED,100:111827&height=95&section=footer" alt="Footer wave" />
</p>
