import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("250x260")

entry = tk.Entry(root, justify='right', font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


def add_entry(text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + text)


def clear_entry():
    entry.delete(0, tk.END)


def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (txt, r, c) in buttons:
    if txt == '=':
        btn = tk.Button(root, text=txt, width=6, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=txt, width=6, height=2,
                        command=lambda t=txt: add_entry(t))
    btn.grid(row=r, column=c, padx=2, pady=2)

clear_btn = tk.Button(root, text='C', width=22, command=clear_entry)
clear_btn.grid(row=5, column=0, columnspan=4, pady=8)

root.mainloop()
