import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    if length < 1:
        messagebox.showerror("Error", "Password length must be at least 1")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


window = tk.Tk()
window.title("Password Generator")


length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=5)
length_entry.insert(0, "12")  

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)


password_entry = tk.Entry(window, width=30, state="readonly")
password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()