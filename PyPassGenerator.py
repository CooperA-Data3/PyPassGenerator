import tkinter as tk
import string
import random
import pyperclip

# Create the tkinter application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("350x350")

# Create a label for the password length slider
length_label = tk.Label(app, text="Password Length:")
length_label.grid(row=0, column=0, pady=5, padx=5)

# Create a slider for the password length
length_slider = tk.Scale(app, from_=8, to=32, orient=tk.HORIZONTAL, length=200)
length_slider.grid(row=0, column=1, pady=5, padx=5)

# Create a label for the password strength radio buttons
strength_label = tk.Label(app, text="Password Strength:")
strength_label.grid(row=1, column=0, pady=5, padx=5)

# Create a frame for the password strength radio buttons
strength_frame = tk.Frame(app)
strength_frame.grid(row=1, column=1, pady=5, padx=5)

# Create the password strength radio buttons
strength_var = tk.StringVar()
strength_var.set("easy")

easy_button = tk.Radiobutton(strength_frame, text="Low", variable=strength_var, value="easy")
easy_button.pack(side=tk.LEFT)

medium_button = tk.Radiobutton(strength_frame, text="Medium", variable=strength_var, value="medium")
medium_button.pack(side=tk.LEFT)

hard_button = tk.Radiobutton(strength_frame, text="High", variable=strength_var, value="hard")
hard_button.pack(side=tk.LEFT)

# Create a label for the generated password
password_label = tk.Label(app, text="")
password_label.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

# Create a function to generate a password
def generate_password():
    length = length_slider.get()
    strength = strength_var.get()

    if strength == "easy":
        chars = string.ascii_lowercase + string.digits
    elif strength == "medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(chars) for _ in range(length))
    password_label.config(text=password)

# Create a button to generate a password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=5, padx=5)
# Create a function to copy the generated password to the clipboard
def copy_password():
    password = password_label.cget("text")
    pyperclip.copy(password)

# Create a button to copy the generated password to the clipboard
copy_button = tk.Button(app, text="Copy Password to Clipboard", command=copy_password)
copy_button.grid(row=4, column=0, columnspan=2, pady=5, padx=5)
# Run the tkinter application window
app.mainloop()

