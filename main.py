import tkinter as tk


def button_action():
    print("Кнопка нажата!")


root = tk.Tk()
root.title("Приложение с кнопками")

label = tk.Label(root, text="Это приложение с кнопками.")
label.pack()

button = tk.Button(root, text="Нажми меня!", command=button_action)
button.pack()

root.mainloop()

