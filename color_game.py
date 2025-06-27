import tkinter as tk
from tkinter import messagebox
import random
import os
from playsound import playsound  # install via pip
import threading

# Game Settings
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30
highscore = 0
difficulty = "Medium"

# Load high score from file
def loadHighScore():
    global highscore
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            try:
                highscore = int(file.read())
            except:
                highscore = 0

def saveHighScore():
    with open("highscore.txt", "w") as file:
        file.write(str(highscore))

def playSound():
    try:
        threading.Thread(target=playsound, args=("ding.mp3",), daemon=True).start()
    except:
        pass  # No sound file or error in playing

def setDifficulty(level):
    global difficulty, timeleft
    difficulty = level
    if level == "Easy":
        timeleft = 60
    elif level == "Medium":
        timeleft = 30
    else:
        timeleft = 15
    resetGame()

def resetGame():
    global score, timeleft
    score = 0
    score_label.config(text="Score: 0")
    time_label.config(text="Time left: " + str(timeleft))
    entry.delete(0, tk.END)
    entry.focus_set()
    color_label.config(text="")
    message_label.config(text="")
    
def startGame(event=None):
    if timeleft > 0 and not game_running.get():
        game_running.set(True)
        countdown()
    nextColor()

def nextColor():
    global score, timeleft, highscore

    if timeleft > 0:
        entry.focus_set()

        if entry.get().lower() == colors[1].lower():
            score += 1
            playSound()

        entry.delete(0, tk.END)
        random.shuffle(colors)

        color_label.config(fg=str(colors[1]), text=str(colors[0]))
        score_label.config(text="Score: " + str(score))

def countdown():
    global timeleft, highscore

    if timeleft > 0:
        timeleft -= 1
        time_label.config(text="Time left: " + str(timeleft))
        root.after(1000, countdown)
    else:
        game_running.set(False)
        if score > highscore:
            highscore = score
            saveHighScore()
            message_label.config(text="🎉 New High Score!")
        else:
            message_label.config(text="Time's up!")
        highscore_label.config(text=f"High Score: {highscore}")

# GUI Setup
root = tk.Tk()
root.title("Color Game - Enhanced Edition")
root.geometry("500x350")
root.resizable(False, False)

game_running = tk.BooleanVar()
game_running.set(False)

# Load existing high score
loadHighScore()

# Layout
tk.Label(root, text="Type the COLOR of the word, not the word itself!", font=('Helvetica', 14)).pack(pady=5)

frame = tk.Frame(root)
frame.pack()

score_label = tk.Label(frame, text="Score: 0", font=('Helvetica', 12))
score_label.grid(row=0, column=0, padx=10)

highscore_label = tk.Label(frame, text=f"High Score: {highscore}", font=('Helvetica', 12))
highscore_label.grid(row=0, column=1, padx=10)

time_label = tk.Label(root, text="Time left: 30", font=('Helvetica', 12))
time_label.pack()

color_label = tk.Label(root, font=('Helvetica', 60))
color_label.pack(pady=10)

entry = tk.Entry(root, font=('Helvetica', 16))
entry.pack()
entry.focus_set()

message_label = tk.Label(root, font=('Helvetica', 12), fg="green")
message_label.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Reset", command=resetGame, width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Easy", command=lambda: setDifficulty("Easy"), width=10).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Medium", command=lambda: setDifficulty("Medium"), width=10).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Hard", command=lambda: setDifficulty("Hard"), width=10).grid(row=0, column=3, padx=5)

# Key binding
root.bind('<Return>', startGame)

root.mainloop()
