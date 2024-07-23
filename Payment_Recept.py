import tkinter as tk
from tkinter import messagebox

class PaymentReceiptApp(tk.Tk):
    info = []
    def __init__(self):
        super().__init__()
        self.title("Payment Receipt App")
        self.geometry("400x600")
        self.configure(bg='lightblue')

        self.create_widgets()
    
    def create_widgets(self):
        # Title
        tk.Label(self, text="Payment Receipt", font=("Arial", 16), bg='lightblue').pack(pady=10)
        
        # Form Fields
        form_frame = tk.Frame(self, bg='lightblue')
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="Name:", font=("Arial", 12), bg='lightblue').grid(row=0, column=0, sticky='w')
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(form_frame, text="Amount:", font=("Arial", 12), bg='lightblue').grid(row=1, column=0, sticky='w')
        self.amount_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.amount_entry.grid(row=1, column=1, pady=5)
        
        tk.Label(form_frame, text="Payment Method:", font=("Arial", 12), bg='lightblue').grid(row=2, column=0, sticky='w')
        self.payment_method_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.payment_method_entry.grid(row=2, column=1, pady=5)
        
        tk.Label(form_frame, text="Date:", font=("Arial", 12), bg='lightblue').grid(row=3, column=0, sticky='w')
        self.date_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.date_entry.grid(row=3, column=1, pady=5)

        # Generate Receipt Button
        tk.Button(self, text="Generate Receipt", command=self.generate_receipt, font=("Arial", 12), bg='white').pack(pady=10)
        
        # Receipt Display
        self.receipt_text = tk.Text(self, font=("Arial", 12), height=15, width=40, bg='lightyellow')
        self.receipt_text.pack(pady=10)
        
        #Generate info button
        tk.Button(self, text="Show Info", command=self.Show_Info, font=("Arial", 12), bg='white').pack(pady=10)
    
    def generate_receipt(self):
        # Fetch form data
        name = self.name_entry.get()
        amount = self.amount_entry.get()
        payment_method = self.payment_method_entry.get()
        date = self.date_entry.get()
        
        # Validate inputs
        if not name or not amount or not payment_method or not date:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")
            return
        
        # Generate receipt text
        receipt = (
            f"-------- Payment Receipt --------\n"
            f"Name: {name}\n"
            f"Amount: ${amount:.2f}\n"
            f"Payment Method: {payment_method}\n"
            f"Date: {date}\n"
            f"----------------------------------\n"
            f"Thank you for your payment!"
        )
        
        # Display receipt
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(tk.END, receipt)
        
        while True:
            self.info.append(receipt)
            return(self.info)

    def Show_Info(self):
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(tk.END, self.info)

# if __name__ == "__main__":
app = PaymentReceiptApp()
app.mainloop()