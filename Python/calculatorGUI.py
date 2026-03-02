import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("320x420")
        self.resizable(False, False)
        self.configure(bg="#222")
        self._create_widgets()

    def _create_widgets(self):
        self.expression = ""
        self.input_text = tk.StringVar()

        # Entry widget
        entry = ttk.Entry(self, textvariable=self.input_text, font=("Segoe UI", 24), justify='right', state='readonly')
        entry.pack(fill='x', padx=10, pady=20, ipady=10)

        # Button layout
        btns = [
            ["C", "/", "*", "<-"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "(", ")"]
        ]

        btn_frame = tk.Frame(self, bg="#222")
        btn_frame.pack(expand=True, fill='both')

        for r, row in enumerate(btns):
            for c, char in enumerate(row):
                btn = tk.Button(
                    btn_frame, text=char, font=("Segoe UI", 18), width=5, height=2,
                    bg="#333", fg="#fff", bd=0, activebackground="#444", activeforeground="#0f0",
                    command=lambda ch=char: self._on_button_click(ch)
                )
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)
        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)

    def _on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "<-":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
