import random
import tkinter as tk
from tkinter import filedialog, messagebox


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b



def show_greeting():
    my_name = name_entry.get()
    hello = f"Привет, {my_name}"
    messagebox.showinfo("Приветствие", hello)
    root.deiconify()





def input_name_window():
    name_window = tk.Toplevel(root)
    name_window.title("Введите ваше имя")
    name_window.geometry("300x150")

    global name_entry
    name_entry = tk.Entry(name_window)
    name_entry.pack(pady=20)

    submit_button = tk.Button(name_window, text="Подтвердить", command=show_greeting)
    submit_button.pack(pady=10)



def vibor_file():
    global name
    name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if name:
        random_numbers_file()


def random_numbers_file():
    with open(name, 'w') as file:
        for i in range(10):
            numbers = random.randint(0, 999)
            file.write(f"{numbers}\n")
    read_file_srednee()


def read_file_srednee():
    with open(name, "r") as file:
        read_file = []
        for g in file:
            numbers_file = int(g.strip())
            read_file.append(numbers_file)
            print(numbers_file)
        sum_number = sum(read_file)
        len_number = len(read_file)
        srednee = sum_number // len_number if len_number > 0 else 0
        print('Среднее значение чисел: ', srednee)


def save_input_number():
    input_number = entry.get()
    with open(name, 'a') as file:
        file.write(f"{input_number}\n")
    read_file_srednee()


def mini_calculator(operation):
    try:
        one_number = float(entry1.get())
        two_number = float(entry2.get())
        calc = Calculator()

        if operation == 'add':
            result = calc.add(one_number, two_number)
        elif operation == 'subtract':
            result = calc.subtract(one_number, two_number)
        elif operation == 'divide':
            result = calc.divide(one_number, two_number)

        output_label.config(text=f"Результат: {result}")
    except ValueError:
        output_label.config(text="Ошибка")



root = tk.Tk()
root.title("Файлы")
root.geometry("500x500+400+200")
name = ""



button = tk.Button(root, text="Выбрать файл", command=vibor_file)
button.pack(pady=30)

entry = tk.Entry(root)
entry.pack(pady=30)

input_button = tk.Button(root, text="Вписать число", command=save_input_number)
input_button.pack(pady=10)

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

entry1 = tk.Entry(root)
entry1.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

calc_add_button = tk.Button(root, text="Сложить", command=lambda: mini_calculator('add'))
calc_add_button.pack(pady=5)

calc_subtract_button = tk.Button(root, text="Вычесть", command=lambda: mini_calculator('subtract'))
calc_subtract_button.pack(pady=5)

calc_divide_button = tk.Button(root, text="Разделить", command=lambda: mini_calculator('divide'))
calc_divide_button.pack(pady=5)


root.withdraw()

input_name_window()

root.mainloop()
