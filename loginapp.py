import tkinter as tk
from tkinter import messagebox

users = {}

app = tk.Tk()
app.title('USER LOGIN APP')
app.geometry('600x500')
app.config(bg='#FFB0E2')

def clear_frame():
    for widget in app.winfo_children():
        widget.destroy()

def create_entry(parent, placeholder, show=None):
    entry = tk.Entry(parent, font=('Segoe UI', 12), bd =0,bg='#e2e8f0', fg="#f700ff", width=30)
    entry.insert(0, placeholder)

    def on_focus_in(e):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="#ec9eff")
            if show:
                entry.config(show = show)

    def on_focus_out(e):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#45daff")
    
    entry.bind('<FocusIn>', on_focus_in)
    entry.bind('<FocusOut>', on_focus_out)

    return entry

def show_login():
    clear_frame()

    container = tk.Frame(app, bg="#ec9eff")
    container.pack(expand = True)

    card = tk.Frame(container, bg= "#f52a8f", padx=40, pady=40)
    card.pack()

    title = tk.Label(card, text='Welcome Back', font=('Segoe UI', 20, "bold"))
    title.pack(pady=(0, 20))

    username = create_entry(card, "Username")
    username.pack(pady=10, ipady=6)

    password = create_entry(card, "Password", show ="*")
    password.pack(pady=10, ipady=6)
    
    def login_user():
        u = username.get()
        p = password.get()

        if u in users and users[u]["password"] == p:
            messagebox.showinfo("Success", f"Welcome {users[u]['name']}")
        else:
            messagebox.showerror("Error", "Invalid credentials")

    login_btn = tk.Button(card, text="Login", bg="#ad9eff", fg="white", font=("Segoe UI", 11, "bold"), width=20, command=login_user)
    login_btn.pack(pady=15, ipady=5)

    switch = tk.Button(card, text="Create new account", bg="#fa72d8", fg="#f2cdfc", bd=0, command=show_signup)
    switch.pack()

def show_signup():
    clear_frame()

    container =  tk.Frame(app, bg= "#ec9eff")
    container.pack(expand=True)

    card = tk.Frame(container, bg="#fd3ead", padx=40, pady=40)
    card.pack()

    title = tk.Label(card, text="Create Account", font=("Segoe UI", 20, "bold"), bg="#cf4af0", fg="white")
    title.pack(pady=(0, 20))

    name = create_entry(card, "Full Name")
    name.pack(pady=10, ipady=6)

    username = create_entry(card, "Username")
    username.pack(pady=10, ipady=6)

    password=create_entry(card, "Password", show="*")
    password.pack(pady=10, ipady=6)

    def register_user():
        n = name.get()
        u = username.get()
        p = password.get()

        if n == "" or u == "" or p =="" or n =="Full Name" or u == "Username" or p == "Password":
            messagebox.showwarning("Warning", "All fields are required")
        elif u in users:
            messagebox.showerror("Error", "Username already exists")
        else:
            users[u] = {"name": n, "password": p}
            messagebox.showinfo("Success", "Account created successfully")
            show_login()

    signup_btn = tk.button(card, text="Sign Up", bg="#f700ff", fg="white", font=("Segoe UI", 11, "bold"), width=20, command=register_user)
    signup_btn.pack(pady=15, ipady=5)

    switch = tk.Button(card, text="Already have an account?", bg="#f700ff", fg="#fdb7ff", bd = 0, command=show_login)
    switch.pack()

show_login()

app.mainloop()



