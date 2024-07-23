import tkinter as tk
import random

class RockPaperScissors(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock-Paper-Scissors Game")
        self.geometry("400x300")
        self.configure(bg="lightblue")
        
        self.methods = {'R': 0, 'P': 1, 'S': 2}
        self.choices = ["Rock", "Paper", "Scissor"]
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="Rock-Paper-Scissors Game", font=("Arial", 16), bg="lightblue").pack(pady=10)
        
        tk.Label(self, text="Choose one:", font=("Arial", 12), bg="lightblue").pack(pady=5)
        
        self.choice_var = tk.StringVar()
        self.choice_var.set("R")
        
        choices_frame = tk.Frame(self, bg="lightblue")
        choices_frame.pack(pady=5)
        
        for text, value in self.methods.items():
            tk.Radiobutton(choices_frame, text=self.choices[value], variable=self.choice_var, value=text, font=("Arial", 12), bg="lightblue").pack(side=tk.LEFT, padx=10)
        
        tk.Button(self, text="Play", command=self.play_game, font=("Arial", 12), bg="white", fg="black").pack(pady=10)
        
        self.result_label = tk.Label(self, text="", font=("Arial", 12), bg="lightblue")
        self.result_label.pack(pady=10)
        
        self.play_again_button = tk.Button(self, text="Play Again", command=self.reset_game, font=("Arial", 12), bg="white", fg="black")
        self.play_again_button.pack(pady=10)
        self.play_again_button.config(state=tk.DISABLED)
    
    def play_game(self):
        computer_choice = random.randint(0, 2)
        player_choice = self.choice_var.get()
        
        player_val = self.methods[player_choice]
        
        result = ""
        if (computer_choice == 0 and player_val == 1) or (computer_choice == 1 and player_val == 2) or (computer_choice == 2 and player_val == 0):
            result = f"It's {self.choices[computer_choice]}! You Win!"
        elif (computer_choice == 1 and player_val == 0) or (computer_choice == 2 and player_val == 1) or (computer_choice == 0 and player_val == 2):
            result = f"It's {self.choices[computer_choice]}! You Lose!"
        else:
            result = f"It's {self.choices[computer_choice]}! It's a Draw!"
        
        self.result_label.config(text=result)
        self.play_again_button.config(state=tk.NORMAL)
    
    def reset_game(self):
        self.result_label.config(text="")
        self.choice_var.set("R")
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop()