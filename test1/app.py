import math
import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("430x520")
        self.root.resizable(False, False)

        self.expression = ""
        self.current_value = tk.StringVar(value="0")

        self.display = tk.Entry(
            root,
            textvariable=self.current_value,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief="flat",
            bg="#f0f0f0",
        )
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        button_data = [
            ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("÷", 1, 3), ("√", 1, 4),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3), ("x²", 2, 4),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3), ("sin", 3, 4),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3), ("cos", 4, 4),
            ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3, 2), ("tan", 5, 4),
        ]

        for item in button_data:
            if len(item) == 3:
                text, row, col = item
                col_span = 1
            else:
                text, row, col, col_span = item

            tk.Button(
                root,
                text=text,
                width=5,
                height=2,
                font=("Arial", 16, "bold"),
                command=lambda t=text: self.on_button_click(t),
            ).grid(row=row, column=col, columnspan=col_span, sticky="nsew", padx=4, pady=4)

        for i in range(5):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value.isdigit() or value in {".", "+", "-", "×", "÷", "%"}:
            if value in {"+", "-", "×", "÷", "%"}:
                self.expression += value
            else:
                if self.current_value.get() == "0" and value != ".":
                    self.current_value.set("")
                self.expression += value
                self.current_value.set(self.expression)
            return

        if value in {"√", "x²", "π", "e", "sin", "cos", "tan"}:
            self.handle_special(value)
            return

        if value == "C":
            self.expression = ""
            self.current_value.set("0")
            return

        if value == "⌫":
            self.expression = self.expression[:-1]
            self.current_value.set(self.expression if self.expression else "0")
            return

        if value == "=":
            try:
                result = self.evaluate(self.expression)
                self.current_value.set(str(result))
                self.expression = str(result)
            except ZeroDivisionError:
                self.current_value.set("Error")
                self.expression = ""
            except Exception:
                self.current_value.set("Error")
                self.expression = ""

    def handle_special(self, value):
        try:
            num = float(self.current_value.get())
        except ValueError:
            self.current_value.set("Error")
            return

        if value == "√":
            result = math.sqrt(num)
        elif value == "x²":
            result = num ** 2
        elif value == "sin":
            result = math.sin(math.radians(num))
        elif value == "cos":
            result = math.cos(math.radians(num))
        elif value == "tan":
            result = math.tan(math.radians(num))
        elif value == "π":
            self.expression = str(math.pi)
            self.current_value.set(str(math.pi))
            return
        elif value == "e":
            self.expression = str(math.e)
            self.current_value.set(str(math.e))
            return
        else:
            self.current_value.set("Error")
            return

        self.expression = str(result)
        self.current_value.set(str(result))

    def evaluate(self, expression):
        if not expression:
            return 0

        expr = expression.replace("×", "*").replace("÷", "/").replace("%", "/100")
        return eval(expr, {"__builtins__": {}}, {"math": math})


def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()

