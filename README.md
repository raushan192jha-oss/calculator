# Basic Calculator (Tkinter GUI)

NextHikes IT Solutions - Project 2

A simple desktop calculator built with Python and Tkinter.

## Features
- Display screen for the equation and result
- Buttons for digits 0-9 and the decimal point
- Addition, subtraction, multiplication, division
- `=` to calculate, `C` to clear, backspace button
- Keyboard support (digits, operators, Enter, Backspace, Esc)
- Error handling (e.g. divide by zero)

## Requirements
Python 3.8+ (Tkinter is included with the standard Python installer).
On Ubuntu/Debian: `sudo apt install python3-tk`

## Run
```
python calculator.py
```

## Screenshots
| Start | Addition | Division |
|---|---|---|
| ![start](screenshots/start.png) | ![add](screenshots/addition.png) | ![mix](screenshots/mix.png) |

## How it works
- `equation` variable stores what the user has typed.
- `click()` adds the pressed button to the equation and updates the screen.
- `calculate()` solves the equation using `eval()` and shows the answer.
- `clear()` and `backspace()` empty the screen or delete the last digit.
- `key_press()` lets the user type from the keyboard.
- `try/except` handles errors such as dividing by zero.

## Tech
Python, Tkinter, Visual Studio Code, GitHub
