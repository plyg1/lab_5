import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class TemperaturePlotGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=1)

        # Параметри за замовчуванням
        self.T = 1.5
        self.K = 0.8
        self.U = 2

        self.setup_gui()

    def setup_gui(self):
        # Параметри введення
        param_frame = tk.Frame(self)
        param_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(param_frame, text="T:").pack(side=tk.LEFT)
        self.T_entry = tk.Entry(param_frame, width=10)
        self.T_entry.insert(0, str(self.T))
        self.T_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(param_frame, text="K:").pack(side=tk.LEFT)
        self.K_entry = tk.Entry(param_frame, width=10)
        self.K_entry.insert(0, str(self.K))
        self.K_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(param_frame, text="U:").pack(side=tk.LEFT)
        self.U_entry = tk.Entry(param_frame, width=10)
        self.U_entry.insert(0, str(self.U))
        self.U_entry.pack(side=tk.LEFT, padx=5)

        # Кнопки
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Button(button_frame, text="Створити файл", command=self.create_file).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Показати графік", command=self.show_plot).pack(side=tk.LEFT, padx=5)

        # Місце для графіка
        self.plot_frame = tk.Frame(self)
        self.plot_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def calculate_temperature(self, n=100):
        """Розрахунок температури за рекурентною формулою"""
        try:
            self.T = float(self.T_entry.get())
            self.K = float(self.K_entry.get())
            self.U = float(self.U_entry.get())
        except ValueError:
            messagebox.showerror("Помилка", "Неправильний формат параметрів")
            return None, None

        t = np.linspace(0, 5 * self.T, n)
        y = np.zeros(n)
        y[0] = 0  # початкова умова

        T0 = t[1] - t[0]  # крок за часом

        for k in range(n - 1):
            y[k + 1] = (1 - T0 / self.T) * y[k] + (T0 / self.T) * self.K * self.U

        return t, y

    def create_file(self):
        t, y = self.calculate_temperature()
        if t is None:
            return

        try:
            with open('lab5.txt', 'w') as f:
                for ti, yi in zip(t, y):
                    f.write(f"{ti}#{yi}\n")
            messagebox.showinfo("Успіх", "Файл створено успішно")
        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка при створенні файлу: {str(e)}")

    def show_plot(self):
        t, y = self.calculate_temperature()
        if t is None:
            return

        # Очищення попереднього графіка
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        # Створення нового графіка
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(t, y, 'b-')
        ax.set_xlabel('Час (с)')
        ax.set_ylabel('Температура (K)')
        ax.set_title('Зміна температури термостата')
        ax.grid(True)

        # Статистика
        stats_text = f"Min t: {min(t):.2f}\nMax t: {max(t):.2f}\n"
        stats_text += f"Min T: {min(y):.2f}\nMax T: {max(y):.2f}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("lab5_2-320-v7-Yablochkov-Ilya")
    root.geometry("800x600")
    app = TemperaturePlotGUI(root)
    root.mainloop()
