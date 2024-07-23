import tkinter as tk
from tkinter import simpledialog, messagebox

class MastermindGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mastermind Game")
        self.geometry("500x400")
        self.configure(bg='lightblue')
        
        self.create_widgets()
        
    def create_widgets(self):
        header_frame = tk.Frame(self, bg='lightblue')
        header_frame.pack(pady=10)
        
        tk.Label(header_frame, text="==== Mastermind Game ====", font=("Arial", 16), bg='lightblue').pack()
        tk.Label(header_frame, text="Enter a number of length 5 between (0 to 9)", bg='lightblue').pack()

        control_frame = tk.Frame(self, bg='lightblue')
        control_frame.pack(pady=20)

        self.btn_start = tk.Button(control_frame, text="Start Game", command=self.start_game, font=("Arial", 12), bg='white', fg='black')
        self.btn_start.grid(row=0, column=0, padx=10)

        self.btn_reset = tk.Button(control_frame, text="Reset Game", command=self.reset_game, font=("Arial", 12), bg='white', fg='black')
        self.btn_reset.grid(row=0, column=1, padx=10)
        self.btn_reset.config(state=tk.DISABLED)

        self.status_label = tk.Label(self, text="", font=("Arial", 12), bg='lightblue')
        self.status_label.pack(pady=10)

        self.attempts_label = tk.Label(self, text="", font=("Arial", 12), bg='lightblue')
        self.attempts_label.pack(pady=10)

        self.hints_label = tk.Label(self, text="", font=("Arial", 12), bg='lightblue')
        self.hints_label.pack(pady=10)
        
    def start_game(self):
        self.btn_start.config(state=tk.DISABLED)
        self.btn_reset.config(state=tk.NORMAL)
        self.status_label.config(text="Player 1: Enter your number")
        self.player1_number = self.get_player_number(1)
        if self.player1_number:
            self.play_game(1, self.player1_number)
        
    def reset_game(self):
        self.btn_start.config(state=tk.NORMAL)
        self.btn_reset.config(state=tk.DISABLED)
        self.status_label.config(text="")
        self.attempts_label.config(text="")
        self.hints_label.config(text="")
        
    def get_player_number(self, player_num):
        while True:
            number = simpledialog.askstring(f"Player {player_num}", f"Enter a number (5 digits):", show='*')
            if number and len(number) == 5 and number.isdigit():
                return number
            messagebox.showerror("Error", "Please enter a number of length 5.")
    
    def play_game(self, player_num, player_number):
        attempts = 0
        hint_given = False
        
        while True:
            guess = simpledialog.askstring("Guess", f"Player {player_num} - Guess a number:")
            if not guess or len(guess) != 5 or not guess.isdigit():
                messagebox.showerror("Error", "Please enter a number of length 5.")
                continue

            attempts += 1
            self.attempts_label.config(text=f"Player {player_num} Attempts: {attempts}")

            if attempts == 5 and not hint_given:
                hint = messagebox.askyesno("Hint", "Do you want a hint?")
                if hint:
                    hint_given = True
                    self.hints_label.config(text=f"Hint: The number starts with {player_number[:2]}***")

            if guess == player_number:
                messagebox.showinfo("Win", f"Player {player_num} Guess number in {attempts} attempts!")
                self.status_label.config(text=f"Player {player_num} Guess number in {attempts} attempts!")
                if player_num == 1:
                    self.attempts1 = attempts
                    self.start_player2_game()
                else:
                    self.attempts2 = attempts
                    self.decide_winner()
                break
            else:
                self.show_correct_digits(player_number, guess)
    
    def show_correct_digits(self, player_number, guess):
        reversed_number = player_number[::-1]
        correct_digits = [digit for digit in reversed_number if digit in guess]
        self.hints_label.config(text=f"Correct digits in guess: {', '.join(correct_digits)}")
    
    def start_player2_game(self):
        self.status_label.config(text="Player 2: Enter your number")
        self.player2_number = self.get_player_number(2)
        if self.player2_number:
            self.play_game(2, self.player2_number)
    
    def decide_winner(self):
        if self.attempts1 < self.attempts2:
            messagebox.showinfo("Result", "Player 1 wins!")
            self.status_label.config(text="Player 1 wins!")
        elif self.attempts1 > self.attempts2:
            messagebox.showinfo("Result", "Player 2 wins!")
            self.status_label.config(text="Player 2 wins!")
        else:
            messagebox.showinfo("Result", "It's a draw!")
            self.status_label.config(text="It's a draw!")
        
if __name__ == "__main__":
    app = MastermindGame()
    app.mainloop()
