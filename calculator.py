import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        self.root.configure(bg="#fa3e9c")

        self.entry = tk.Entry(
            root, font=("Arial", 24, "bold"), borderwidth=5, relief ="ridge",
            justify="right", bg="#ecf0f1", fg="black", insertbackground="black"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

        buttons = [
            ('7', 1, 0, "#bafff1"), ('8', 1, 1, "#bafff1"), ('9', 1, 2, "#bafff1"), ('/', 1, 3, "#ffc5e2"),
            ('4', 2, 0, "#b0e0ff"), ('5', 2, 1, "#b0e0ff"), ('6', 2, 2, "#b0e0ff"), ('*', 2, 3, "#ffc5e2"),
            ('1', 3, 0, "#ecbbff"), ('2', 3, 1, "#ecbbff"), ('3', 3, 2, "#ecbbff"), ('-', 3, 3, "#ffc5e2"),
            ('0', 4, 0, "#ffc5e2"), ('.', 4, 1, "#ffc5e2"), ('C', 4, 2, "#ff41a0"), ('+', 4, 3, "#ffc5e2"),
            ('⌫', 5, 0, "#95a5a6"), ('=', 5, 1, "#bafff1", 3)
        ]

        for (text, row, col, colour, *span) in buttons:
            colspan = span[0] if span else 1
            btn = tk.Button(
                root, text=text, font=("Arial", 18, "bold"),
                command = lambda t=text: self.on_button_click(t),
                bg = colour, fg ="white", activebackground="#34495e", activeforeground = "white",
                relief="raised", bd=4
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3,ipadx=5, ipady=10)

        for i in range(6):
            root.grid_rowconfigure(i,weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        root.bind("<Key>", self.key_handler)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.entry.delete(0,tk.END)
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.entry.delete(tk.END)
            self.entry.insert(tk.END, self.expression)
        elif char =='=':
            try:
                result =str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            if char in "+-*/" and (not self.expression or self.expression[-1] in "+-*/"):
                return
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def key_handler(self, event):
        char = event.char
        if char.isdigit() or char in "+-*/.":
            self.on_button_click(char)
        elif event.keysym == "Return":
            self.on_button_click("=")
        elif event.keysym == "BackSpace":
            self.on_button_click("⌫") 
        elif event.keysym == "Escape":
            self.on_button_click("C")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
