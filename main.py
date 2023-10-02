import tkinter

PINK = "#e2989c"
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ----- Timer Reset -------- #
# ----- Timer Mechanism -------- #
# ----- Countdown Mechanism -------- #

# ----- UI Setup -------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1,column=1)

title = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
title.grid(row=0, column=1)

checkmark = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmark.grid(row=3, column=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, bg=YELLOW, borderwidth=2, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, borderwidth=2, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

window.mainloop()
