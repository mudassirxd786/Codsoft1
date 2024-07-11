import tkinter as tk
from tkinter import messagebox
import random

rock = '''
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)___
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
game_choices = ["Rock", "Paper", "Scissors"]


def play_game(user_choice):
    result_label.config(text="")  # Clearing the  previous result
    computer_choice = random.randint(0, 2)
    user_choice_image.config(text=game_images[user_choice])
    computer_choice_image.config(text=game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        result = "You win!"
    elif computer_choice == 0 and user_choice == 2:
        result = "You lose"
    elif computer_choice > user_choice:
        result = "You lose"
    elif user_choice > computer_choice:
        result = "You win!"
    elif computer_choice == user_choice:
        result = "It's a draw."

    result_label.config(text=result)


def reset_game():
    user_choice_image.config(text="")
    computer_choice_image.config(text="")
    result_label.config(text="")


def play_again():
    reset_game()


def on_exit():
    app.destroy()


app = tk.Tk()
app.title("Rock-Paper-Scissors")

instructions = tk.Label(app, text="Choose Rock, Paper, or Scissors:")
instructions.pack()

buttons_frame = tk.Frame(app)
buttons_frame.pack()

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: play_game(0))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: play_game(1))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: play_game(2))
scissors_button.pack(side=tk.LEFT, padx=10)

user_choice_label = tk.Label(app, text="Your Choice:")
user_choice_label.pack()
user_choice_image = tk.Label(app, text="", font=("Courier", 14))
user_choice_image.pack()

computer_choice_label = tk.Label(app, text="Computer's Choice:")
computer_choice_label.pack()
computer_choice_image = tk.Label(app, text="", font=("Courier", 14))
computer_choice_image.pack()

result_label = tk.Label(app, text="", font=("Courier", 16, "bold"))
result_label.pack()

play_again_button = tk.Button(app, text="Play Again", command=play_again)
play_again_button.pack(pady=5)

exit_button = tk.Button(app, text="Exit", command=on_exit)
exit_button.pack(pady=5)

app.mainloop()
