import tkinter as tk
from task1 import PalindromeGUI
from task2 import TemperaturePlotGUI

task_window_dict = {
    "1": (PalindromeGUI, "lab5_1-320-v16-Yablochkov-Ilya", "400x200"),
    "2": (TemperaturePlotGUI, "lab5_2-320-v7-Yablochkov-Ilya", "800x600")
}

def main():
    choice = input("Будь ласка, оберіть завдання 1-2 (0-ВИХІД): ")
    while choice != "0":
        if choice in task_window_dict.keys():
            application = tk.Tk()
            window_class, window_name, window_size = task_window_dict.get(choice)
            window = window_class(application)
            application.geometry(window_size)
            application.title(window_name)
            application.mainloop()
        else:
            print("Неправильний номер завдання!")
        choice = input("Будь ласка, оберіть завдання знову (0-ВИХІД): ")

if __name__ == '__main__':
    main()
