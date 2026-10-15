# Basic Calculator using Tkinter
# NextHikes IT Solutions - Project 2

from tkinter import *

# This variable stores what the user has typed so far
equation = ""


def show():
    """Shows the equation on the screen (shows 0 if empty)."""
    if equation == "":
        screen.set("0")
    else:
        screen.set(equation)


def click(value):
    """Runs when a number or operator button is pressed."""
    global equation
    equation = equation + value
    show()


def clear():
    """Clears the screen (C button)."""
    global equation
    equation = ""
    show()


def backspace():
    """Deletes the last character."""
    global equation
    equation = equation[:-1]
    show()


def calculate():
    """Calculates the answer (= button)."""
    global equation
    try:
        answer = eval(equation)
        if answer == int(answer):      # 5.0 becomes 5
            answer = int(answer)
        equation = str(answer)
        show()
    except ZeroDivisionError:
        equation = ""
        screen.set("Divide by 0")
    except:
        equation = ""
        screen.set("Error")


def button_press(text):
    """Decides what to do for each button."""
    if text == "C":
        clear()
    elif text == "⌫":
        backspace()
    elif text == "=":
        calculate()
    else:
        click(text)


def key_press(event):
    """Lets the user type from the keyboard."""
    if event.char in "0123456789.+-*/" and event.char != "":
        click(event.char)
    elif event.keysym == "Return" or event.char == "=":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape" or event.char == "c":
        clear()


def make_button(text, row, column, color, columnspan=1, rowspan=1):
    """Creates one button and places it on the window."""
    def action():
        button_press(text)

    Button(window, text=text, font=("Arial", 18), bg=color, fg="white",
           bd=0, activebackground="#6c7086", command=action
           ).grid(row=row, column=column, columnspan=columnspan,
                  rowspan=rowspan, sticky="nsew", padx=3, pady=3)


# ---------- Main window ----------
window = Tk()
window.title("NextHikes Calculator")
window.geometry("320x460")
window.resizable(False, False)
window.configure(bg="#1e1e2e")

# Display area (screen)
screen = StringVar()
screen.set("0")
Entry(window, textvariable=screen, font=("Arial", 28), justify="right",
      bd=0, bg="#2b2b3d", fg="white", readonlybackground="#2b2b3d",
      state="readonly").grid(row=0, column=0, columnspan=4, sticky="nsew",
                             padx=10, pady=15, ipady=15)

# Make rows and columns share the space equally
for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(1, 6):
    window.rowconfigure(i, weight=1)

# Colors
grey = "#45475a"
orange = "#fab387"
pink = "#f38ba8"

# Buttons (text, row, column, color)
make_button("C", 1, 0, pink)
make_button("⌫", 1, 1, orange)
make_button("/", 1, 2, orange)
make_button("*", 1, 3, orange)

make_button("7", 2, 0, grey)
make_button("8", 2, 1, grey)
make_button("9", 2, 2, grey)
make_button("-", 2, 3, orange)

make_button("4", 3, 0, grey)
make_button("5", 3, 1, grey)
make_button("6", 3, 2, grey)
make_button("+", 3, 3, orange)

make_button("1", 4, 0, grey)
make_button("2", 4, 1, grey)
make_button("3", 4, 2, grey)
make_button("=", 4, 3, orange, rowspan=2)

make_button("0", 5, 0, grey, columnspan=2)
make_button(".", 5, 2, grey)

# Keyboard support
window.bind("<Key>", key_press)

window.mainloop()
