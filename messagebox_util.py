import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

def show_messagebox(title, message, mtype):
    try:
        if mtype == "info":
            messagebox.showinfo(title, message)
        elif mtype == "warning":
            messagebox.showwarning(title, message)
        elif mtype == "error":
            messagebox.showerror(title, message)
    except Exception as e:
        print(f"Error showing message: {e}")

