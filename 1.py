from tkinter import *

def change_button_color(button, color):
    button.config(bg=color, fg="white")

root = Tk()

color_codes = [
    ("Red", "#FF0000"),
    ("Orange", "#FFA500"),
    ("Yellow", "#FFFF00"),
    ("Green", "#008000"),
    ("Aquamarine", "#7FFFD4"),
    ("Blue", "#0000FF"),
    ("Purple", "#800080"),
    ("Brown", "#A52A2A"),
    ("Gray", "#808080"),
    ("Black", "#080100")
]

text_frame = Frame(root)
text_frame.grid(padx=10, pady=5)

button_frame = Frame(root)
button_frame.grid(row=0, column=1, padx=10, pady=5)

buttons = []  

for i, (color, code) in enumerate(color_codes):
    label_color = Label(text_frame, text=color, width=10)
    label_color.grid(row=i, column=0, pady=5, sticky="w")

    button = Button(button_frame, text="", bg=code)
    button.config(width=40)
    button.grid(row=i, column=1, pady=2, padx=5)

    label_code = Label(button_frame, text=code, width=10)
    label_code.grid(row=i, column=2, pady=5)

    buttons.append(button)

root.mainloop()








