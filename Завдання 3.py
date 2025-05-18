import tkinter as tk
from tkinter import messagebox
from math import sin, sqrt

def calculate_sum(event = None):
    try:
        x = float(entry_x.get())
        total = 0
        for k in range(1, 13):
            numerator = sin(k * x) + k
            denominator = sqrt(x + 0.1 + 6 * k)
            total += numerator / denominator

        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(round(total, 4)))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректне числове значення для x!")

# Графічний інтерфейс
root = tk.Tk()
root.title("Обчислення суми (варіант 3)")
root.geometry("400x300")

# Зображення 
photo = tk.PhotoImage(file="D:/Університет/інформатика/лабораторна робота 13/зав 3.gif")
label_image = tk.Label(root, image=photo)
label_image.grid(row=0, column=0, columnspan=2, pady=5)

# Введення x
label_x = tk.Label(root, text="Введіть x:")
label_x.grid(row=1, column=0, padx=10, pady=10)
entry_x = tk.Entry(root)
entry_x.grid(row=1, column=1)

# Кнопка обчислення
btn_calc = tk.Button(root, text="Обчислити")
btn_calc.bind('<Button-1>', calculate_sum)
root.bind('<Return>', calculate_sum)
btn_calc.grid(row=2, column=0, columnspan=2, pady=10)

# Результат
label_result = tk.Label(root, text="Результат:")
label_result.grid(row=3, column=0, padx=10, pady=5)
entry_result = tk.Entry(root)
entry_result.grid(row=3, column=1)

root.mainloop()
