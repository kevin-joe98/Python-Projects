import random
import string
import pyperclip  # For copying to clipboard (you'll need to install this package)

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Base character set (lowercase letters are always included)
    characters = string.ascii_lowercase
    
    # Add additional character sets based on user preferences
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage
password = generate_password(length=16, use_uppercase=True, use_digits=True, use_special=True)
print("Generated Password:", password)

# Copy the password to the clipboard
pyperclip.copy(password)
print("Password copied to clipboard!")



import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate the password
def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy the password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")

# Create the GUI window
window = tk.Tk()
window.title("Password Generator")

# Password Length Label and Entry
tk.Label(window, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)

# Checkbox for Uppercase Letters
uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, columnspan=2)

# Checkbox for Digits
digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(window, text="Include Digits", variable=digits_var)
digits_check.grid(row=2, column=0, columnspan=2)

# Checkbox for Special Characters
special_var = tk.BooleanVar()
special_check = tk.Checkbutton(window, text="Include Special Characters", variable=special_var)
special_check.grid(row=3, column=0, columnspan=2)

# Entry to display generated password
password_entry = tk.Entry(window, width=30)
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, padx=10, pady=10)

# Button to copy password to clipboard
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, column=1, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
