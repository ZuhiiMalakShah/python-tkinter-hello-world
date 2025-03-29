import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello, World!")

# Main window create karein
root = tk.Tk()
root.title("Hello World GUI")
root.geometry("300x200")

# Ek label add karein
label = tk.Label(root, text="Click the button below:", font=("Arial", 12))
label.pack(pady=20)

# Ek button banayein
button = tk.Button(root, text="Say Hello", command=show_message, font=("Arial", 12), bg="lightblue")
button.pack()

# Application run karein
root.mainloop()
