# week 7 solutions
import tkinter as tk
print("__________________________________________")
print("exercise 1")

root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(expand=True)

root.mainloop()


print("__________________________________________")
print("exercise 1.1")
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(expand=True)


def close_window():
    root.destroy()


close_btn = tk.Button(root, text="Close", command=close_window)
close_btn.pack()

root.mainloop()


print("__________________________________________")
print("exercise 2")

root = tk.Tk()
root.title("Greetings")
root.geometry("300x200")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack(expand=True)

name_entry = tk.Entry(root)
name_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack(expand=True)


def greet():
    name = name_entry.get()
    result_label.config(text=f"Hello, {name}!")


greet_btn = tk.Button(root, text="Greet Me!", command=greet)
greet_btn.pack()

root.mainloop()


print("__________________________________________")
print("exercise 3")

counter = 0


def increment_counter():
    global counter
    counter += 1
    counter_label.config(text=f"Counter: {counter}")


def decrement_counter():
    global counter
    counter -= 1
    counter_label.config(text=f"Counter: {counter}")


root = tk.Tk()
root.title("counter")
root.geometry("300x200")

counter_label = tk.Label(root, text="Counter: 0", font=("Arial", 14))
counter_label.pack(expand=True)

increment_button = tk.Button(root, text="Increment", command=increment_counter)
increment_button.pack(expand=True)

decrement_button = tk.Button(root, text="Decrement", command=decrement_counter)
decrement_button.pack(expand=True)

root.mainloop()


print("__________________________________________")
print("exercise 4")

root = tk.Tk()
root.title("")
root.geometry("300x200")

top_bar = tk.Frame(root, bg="red", height=50)
top_bar.pack(side="top", fill="x")

centre = tk.Frame(root, bg="green")
centre.pack(fill="both", expand=True)

bottom_bar = tk.Frame(root, bg="blue", height=50)
bottom_bar.pack(side="bottom", fill="x")

root.mainloop()


print("__________________________________________")
print("exercise 5")

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
