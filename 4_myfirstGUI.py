import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.expression = ""
        self.ent = ctk.CTkEntry(self, width=260, height=50, font=("Arial", 20))
        self.ent.pack(pady=20)
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]
        frame = ctk.CTkFrame(self)
        frame.pack()
        for i, btn in enumerate(buttons):
            button = ctk.CTkButton(
                frame,
                text=btn,
                width=60,
                height=60,
                command=lambda b=btn: self.click(b)
            )
            button.grid(row=i//4, column=i%4, padx=5, pady=5)
    def click(self, value):
        if value == "C":
            self.expression = ""
        elif value == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += value
        self.ent.delete(0, "end")
        self.ent.insert(0, self.expression)  
app = Calculator()
app.mainloop()
