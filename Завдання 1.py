import tkinter as tk
from math import sqrt

def calculate_function(event=None):
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    result = ((-b - sqrt(b**2 + 4*a*c)) / 2*a) + abs(c)
    format_result = "{:.2f}".format(result)  # Вивести з точністю до 2 знаків після коми
    label_result.config(text="Результат: " + format_result)  # Оновити текст в Label

root = tk.Tk()
root.title("Функція")
root.geometry("300x300")

# Зображення
photo = tk.PhotoImage(file="D:/Університет/інформатика/лабораторна робота 13/зав 1.gif")
label_image = tk.Label(root, image=photo)
label_image.grid(row=0, column=0, columnspan=2, pady=10)

# Введення a
label_a = tk.Label(root, text="Введіть значення a:")
label_a.grid(row=1, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1, padx=5, pady=5)

# Введення b
label_b = tk.Label(root, text="Введіть значення b:")
label_b.grid(row=2, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1, padx=5, pady=5)

# Введення c
label_c = tk.Label(root, text="Введіть значення c:")
label_c.grid(row=3, column=0, padx=5, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=3, column=1, padx=5, pady=5)

# Кнопка обчислення
button_calculate = tk.Button(root, text="Обчислити", command=calculate_function)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Вивід результату
label_result = tk.Label(root, text="")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()