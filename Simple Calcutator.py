import tkinter as tk

def button_click(value):
    if value == "=":
        try:
            expression = entry.get()
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("My first project")
root.config(bg="lightgray")

entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid", bg="lightblue")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

for i, btn in enumerate(buttons):
    tk.Button(root, text=btn, width=5, height=2, font=("Arial", 14, "bold") if btn.isdigit() else ("Arial", 14),
              fg="red" if btn == "C" else "black",
              bg="lightblue",
              command=lambda b=btn: button_click(b)).grid(row=1 + i // 4, column=i % 4, padx=5, pady=5)

root.mainloop()