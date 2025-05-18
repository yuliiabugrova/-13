import tkinter as tk
from tkinter import messagebox
from math import sqrt

def calculate(event=None):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Перевірка існування трикутника
        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2  # Півпериметр
            area = sqrt(s * (s - a) * (s - b) * (s - c))  # Площа за формулою Герона

            r = area / s  # Радіус вписаного кола
            w_a = sqrt(b * c * (1 - (a**2) / ((b + c)**2)))  # Бісектриса до сторони a

            entry_radius.delete(0, tk.END)
            entry_radius.insert(0, str(round(r, 2)))

            entry_bisectrix.delete(0, tk.END)
            entry_bisectrix.insert(0, str(round(w_a, 2)))
        else:
            messagebox.showerror("Помилка", "Трикутник із заданими сторонами не існує!")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення для сторін трикутника!")

# Інтерфейс
root = tk.Tk()
root.title("Розрахунок r і wₐ")
root.geometry("400x250")

label_a = tk.Label(root, text="Сторона a:")
label_a.place(x=20, y=20)
entry_a = tk.Entry(root)
entry_a.place(x=150, y=20)

label_b = tk.Label(root, text="Сторона b:")
label_b.place(x=20, y=60)
entry_b = tk.Entry(root)
entry_b.place(x=150, y=60)

label_c = tk.Label(root, text="Сторона c:")
label_c.place(x=20, y=100)
entry_c = tk.Entry(root)
entry_c.place(x=150, y=100)

button_calc = tk.Button(root, text="Обчислити")
button_calc.place(x=150, y=140)

label_radius = tk.Label(root, text="Радіус впис. кола (r):")
label_radius.place(x=20, y=180)
entry_radius = tk.Entry(root)
entry_radius.place(x=150, y=180)

label_bisectrix = tk.Label(root, text="Бісектриса wₐ:")
label_bisectrix.place(x=20, y=210)
entry_bisectrix = tk.Entry(root)
entry_bisectrix.place(x=150, y=210)

button_calc.bind('<Button-1>', calculate)
root.bind('<Return>', calculate)
root.mainloop()