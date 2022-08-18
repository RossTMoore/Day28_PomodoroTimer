from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_base, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(number):
    global timer
    count_min = math.floor(number / 60)
    count_sec = number % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_base, text=f"{count_min}:{count_sec}")
    if number > 0:
        timer = window.after(1000, count_down, number - 1)
    else:
        timer_start()
        if reps % 2 == 0:
            checks["text"] +="✔"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato_img)
timer_base = canvas.create_text(110, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column = 1)

#Labels
timer_label = Label(text="Timer", bg=YELLOW, highlightthickness=0)
timer_label.config(fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

checks = Label(bg=YELLOW, fg=GREEN)
checks.grid(row=3, column=1)

#Buttons
start_button = Button(text="Start", command=timer_start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=2, column=2)


#---LAST LINE___#
window.mainloop()