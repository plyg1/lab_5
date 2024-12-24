import tkinter as tk
from tkinter import messagebox


class PalindromeGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=1)

        # Конфігурація сітки
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)

        # Створення віджетів
        self.create_widgets()

    def create_widgets(self):
        # Мітка та поле введення
        self.label = tk.Label(self, text="Введіть числа:")
        self.label.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)

        # Кнопка перевірки
        self.check_button = tk.Button(self, text="Перевірити", command=self.check_numbers)
        self.check_button.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        # Поле результатів
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self, textvariable=self.result_var)
        self.result_label.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

    def is_palindrome(self, K):
        """Перевіряє, чи є число паліндромом"""
        if K <= 0:
            return False
        num_str = str(K)
        return num_str == num_str[::-1]

    def check_numbers(self):
        """Перевіряє введені числа на паліндромність"""
        try:
            numbers = [int(x) for x in self.entry.get().split()]
            if len(numbers) != 10:
                raise ValueError("Потрібно ввести 10 чисел")
            palindrome_count = sum(1 for num in numbers if self.is_palindrome(num))
            self.result_var.set(f"Кількість паліндромів: {palindrome_count}")
        except ValueError as e:
            messagebox.showerror("Помилка", str(e))
        except Exception as e:
            messagebox.showerror("Помилка", "Неправильний формат введення")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("lab5_1-320-v16-Yablochkov-Ilya")
    root.geometry("400x200")
    app = PalindromeGUI(root)
    root.mainloop()
