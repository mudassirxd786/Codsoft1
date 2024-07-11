import tkinter as tk  #library for gui
from tkinter import messagebox  #for showing alerts
import random # for generating random numbers   
import string


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Atleast one character set must be selected.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password


def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length should be a positive integer")

        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        result_label.config(text="Generated Password: " + password)
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))


app = tk.Tk()
app.title("Password Generator")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

length_label = tk.Label(frame, text="Enter the desired length for the password:")
length_label.pack(pady=5)

length_entry = tk.Entry(frame)
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(frame, text="Uppercase Letters", variable=uppercase_var)
uppercase_check.pack(pady=5)

lowercase_check = tk.Checkbutton(frame, text="Lowercase Letters", variable=lowercase_var)
lowercase_check.pack(pady=5)

digits_check = tk.Checkbutton(frame, text="Include Digits", variable=digits_var)
digits_check.pack(pady=5)

special_check = tk.Checkbutton(frame, text="Special Characters", variable=special_var)
special_check.pack(pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate)
generate_button.pack(pady=5)

result_label =tk.Label(frame, text=" ")
result_label.pack(pady=5)

app.mainloop()
