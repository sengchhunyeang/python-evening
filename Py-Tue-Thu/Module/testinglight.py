import tkinter as tk
from tkinter import messagebox

def login():
    user = username.get()
    pwd = password.get()

    if user == "admin" and pwd == "123":
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")


root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Username
username = tk.Entry(root)
username.insert(0, "Username")
username.pack(pady=10)

# Password
password = tk.Entry(root, show="*")
password.insert(0, "123")
password.pack(pady=10)

# Login Button
btn = tk.Button(root, text="Login", command=login)
btn.pack(pady=10)

root.mainloop()
