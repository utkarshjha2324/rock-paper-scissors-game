import tkinter as tk
from tkinter import ttk
import random

# Initialize scores and game history
win = 0
lose = 0
history = []

# Function to handle game logic
def play_rps(user_choice):
    global win, lose
    computer_choice = random.randint(1, 3)
    choices = ["Rock", "Paper", "Scissors"]

    # Result message
    result_text = f"You chose {choices[user_choice-1]}, I chose {choices[computer_choice-1]}. "

    # Determine game result
    if user_choice == computer_choice:
        result_text += "It's a draw!"
        result_color = "#4ea8de"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        result_text += "You win!"
        win += 1
        result_color = "#27ae60"
    else:
        result_text += "You lose!"
        lose += 1
        result_color = "#e74c3c"

    # Update display and history
    result_var.set(result_text)
    result_label.config(fg=result_color)
    wins_var.set(f"Wins: {win}")
    losses_var.set(f"Losses: {lose}")
    history.append(result_text)

# Reset scores and history
def reset_score():
    global win, lose, history
    win = 0
    lose = 0
    history = []
    result_var.set("Welcome! Choose your move to start playing.")
    result_label.config(fg="black")
    wins_var.set(f"Wins: {win}")
    losses_var.set(f"Losses: {lose}")
    history_var.set("Game History: None")

# Toggle theme
def toggle_theme():
    if theme_button.config('text')[-1] == 'Dark Mode':
        top.config(bg="#34495e")
        result_label.config(bg="#34495e", fg="#ecf0f1")
        title_label.config(bg="#2c3e50", fg="#ecf0f1")
        score_frame.config(bg="#2c3e50")
        history_frame.config(bg="#2c3e50")
        theme_button.config(text="Light Mode", bg="#bdc3c7", fg="black")
    else:
        top.config(bg="#ffffff")
        result_label.config(bg="#ffffff", fg="black")
        title_label.config(bg="#4ea8de", fg="#ffffff")
        score_frame.config(bg="#f7f9fb")
        history_frame.config(bg="#f7f9fb")
        theme_button.config(text="Dark Mode", bg="#2c3e50", fg="white")

# Display game history
def show_history():
    if history:
        history_var.set("Game History:\n" + "\n".join(history[-5:]))  # Show last 5 games
    else:
        history_var.set("Game History: None")

# Set up main window
top = tk.Tk()
top.title("Rock-Paper-Scissors")
top.geometry("600x550")
top.config(bg="#ffffff")

# Gradient background effect
def create_gradient():
    for i in range(100):
        color = f"#{int(255 - i * 1.5):02x}{int(230 - i * 1.5):02x}{255:02x}"
        top_canvas.create_line(0, i*4, 600, i*4, fill=color, width=4)

top_canvas = tk.Canvas(top, width=600, height=400, highlightthickness=0)
top_canvas.place(x=0, y=0)
create_gradient()

# Title label
title_label = tk.Label(
    top, text="Rock-Paper-Scissors", font=("Helvetica", 24, "bold"), bg="#4ea8de", fg="#ffffff", relief="solid", bd=0,
    padx=20, pady=5
)
title_label.place(relx=0.5, y=30, anchor="center")

# Frame for choices
choices_frame = tk.Frame(top, bg="#ffffff")
choices_frame.place(relx=0.5, y=150, anchor="center")

# Function to add button hover effect
def on_enter(e):
    e.widget['background'] = "#4ea8de"
    e.widget['foreground'] = "white"

def on_leave(e):
    e.widget['background'] = "#ffffff"
    e.widget['foreground'] = "black"

# Creating buttons for choices with hover effects
choices = ["Rock", "Paper", "Scissors"]
for index, choice in enumerate(choices):
    button = tk.Button(
        choices_frame, text=choice, font=("Arial", 14, "bold"), width=10, height=2,
        bg="#ffffff", fg="black", bd=0, relief="ridge", cursor="hand2",
        command=lambda choice=index+1: play_rps(choice)
    )
    button.grid(row=0, column=index, padx=10, pady=5)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Result display label
result_var = tk.StringVar()
result_var.set("Welcome! Choose your move to start playing.")
result_label = tk.Label(
    top, textvariable=result_var, font=("Helvetica", 14), bg="#ffffff", wraplength=500, justify="center"
)
result_label.place(relx=0.5, y=220, anchor="center")

# Scoreboard frame
score_frame = tk.Frame(top, bg="#f7f9fb", bd=2, relief="groove", padx=20, pady=10)
score_frame.place(relx=0.5, y=280, anchor="center")

# Score labels
wins_var = tk.StringVar()
losses_var = tk.StringVar()
wins_var.set(f"Wins: {win}")
losses_var.set(f"Losses: {lose}")

wins_label = tk.Label(score_frame, textvariable=wins_var, font=("Arial", 12), bg="#f7f9fb", fg="#27ae60", padx=10)
wins_label.grid(row=0, column=0)

losses_label = tk.Label(score_frame, textvariable=losses_var, font=("Arial", 12), bg="#f7f9fb", fg="#e74c3c", padx=10)
losses_label.grid(row=0, column=1)

# Reset button
reset_button = tk.Button(top, text="Reset Score", command=reset_score, font=("Arial", 12), bg="#f7c41c", fg="black", width=12)
reset_button.place(relx=0.4, y=350, anchor="center")

# Show History button
history_button = tk.Button(top, text="Show History", command=show_history, font=("Arial", 12), bg="#bdc3c7", width=12)
history_button.place(relx=0.6, y=350, anchor="center")

# Theme Toggle Button
theme_button = tk.Button(top, text="Dark Mode", command=toggle_theme, font=("Arial", 12), bg="#2c3e50", fg="white", width=12)
theme_button.place(relx=0.5, y=400, anchor="center")

# Game History display
history_var = tk.StringVar()
history_var.set("Game History: None")
history_frame = tk.Frame(top, bg="#f7f9fb", bd=2, relief="groove", padx=10, pady=10)
history_frame.place(relx=0.5, y=470, anchor="center")
history_label = tk.Label(history_frame, textvariable=history_var, font=("Arial", 10), bg="#f7f9fb", wraplength=500, justify="left")
history_label.grid()

# Start main event loop
top.mainloop()
