import tkinter as tk
from tkinter import messagebox

#Function for Calculator App 
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple  Calculator")

        
        self.num1_entry = tk.Entry(root, width=20)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num2_entry = tk.Entry(root, width=20)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        
        tk.Label(root, text="Number 1:").grid(row=0,column=0,padx=10, pady=10)
        tk.Label(root, text="Number 2:").grid(row=1,column=0,padx=10, pady=10)

        
        tk.Button(root, text="+", width=5, command=self.add).grid(row=2,column=0, padx=10, pady=10)
        tk.Button(root, text="-", width=5, command=self.subtract).grid(row=2,column=1, padx=10, pady=10)
        tk.Button(root, text="*", width=5, command=self.multiply).grid(row=2,column=2, padx=10, pady=10)
        tk.Button(root, text="/", width=5, command=self.divide).grid(row=2,column=3, padx=10, pady=10)

        
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.result_label.config(text=f"Result: {result}")
    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 != 0:
                result = num1 / num2
                self.result_label.config(text=f"Result: {result}")
            else:
                messagebox.showerror("Math Error","Cannot divide by zero.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
