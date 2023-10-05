import tkinter
import time
import math

PINK = "#e2989c"
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 20
SHORT_BREAK_MIN = 7
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ----- Timer Reset -------- #
def reset_timer():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  title.config(text="Timer")
  checkmark.config(text="")
  global reps
  reps = 0
# ----- Timer Mechanism -------- #
def start_timer():
  global reps
  reps += 1
  if reps % 2 == 0:
    if reps % 8 == 0:
      count_down(LONG_BREAK_MIN * 60)
      title.config(text="Long Break", fg=RED)
    else:
      count_down(SHORT_BREAK_MIN * 60)
      title.config(text="Short Break", fg=PINK)
  else:
    count_down(WORK_MIN * 60)
    title.config(text="Work", fg=GREEN)
# ----- Countdown Mechanism -------- #
def count_down(count):
  seconds = count % 60
  minutes = math.floor(count / 60)
  # print(seconds)
  # print(minutes)

  canvas.itemconfig(timer_text, text=f"{'{:02d}'.format(minutes)}:{'{:02d}'.format(seconds)}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  elif count == 0:
    start_timer()
    marks = ""
    for _ in range(math.floor(reps/2)):
      marks += "✔"
    checkmark.config(text=marks)


# ----- UI Setup -------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# def say_something(thing):
#   print(thing)

# window.after(1000, say_something, 'hey')

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1,column=1)


title = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
title.grid(row=0, column=1)

checkmark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmark.grid(row=3, column=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, bg=YELLOW, borderwidth=2, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, borderwidth=2, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()

#end of program
#addtional features
